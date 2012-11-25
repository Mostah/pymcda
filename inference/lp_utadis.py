from __future__ import division
import bisect
import sys
sys.path.insert(0, "..")
from mcda.types import point, segment, piecewise_linear
from mcda.types import category_value, categories_values
from tools.generate_random import generate_random_criteria_values
from tools.generate_random import generate_random_criteria_functions


try:
    solver = os.environ['SOLVER']
except:
    solver = 'cplex'

#if solver == 'glpk':
#    import pymprog
#elif solver == 'scip':
#    from zibopt import scip
if solver == 'cplex':
    import cplex
else:
    raise NameError('Invalid solver selected')

class lp_utadis(object):

    def __init__(self, cs, cat, gi_worst, gi_best):
        self.cs = cs
        self.cat = { cat: i+1 \
                     for i, cat in enumerate(cat.get_ordered_categories()) }
        self.gi_worst = gi_worst
        self.gi_best = gi_best
        self.__compute_abscissa()

        if solver == 'cplex':
            self.lp = cplex.Cplex()

    def __compute_abscissa(self):
        self.points = {}
        for cs in self.cs:
            best = self.gi_best.performances[cs.id]
            worst = self.gi_worst.performances[cs.id]
            diff = best - worst

            self.points[cs.id] = [ worst ]
            for i in range(1, cs.value):
                self.points[cs.id].append(worst + i / cs.value * diff)
            self.points[cs.id].append(best)

    def __get_left_points(self, cid, x):
        left = bisect.bisect_right(self.points[cid], x) - 1
        if left == len(self.points[cid]) - 1:
            left -= 1
        return left

    def add_variables_cplex(self, aids):
        self.lp.variables.add(names = ['x_' + aid for aid in aids],
                              lb = [0 for aid in aids],
                              ub = [1 for aid in aids])
        self.lp.variables.add(names = ['y_' + aid for aid in aids],
                              lb = [0 for aid in aids],
                              ub = [1 for aid in aids])

        self.l_vars = []
        for cs in self.cs:
            cid = cs.id
            nseg = cs.value
            self.lp.variables.add(names = ['w_' + cid + "_%d" % (i+1)
                                           for i in range(nseg)],
                                  lb = [0 for i in range(nseg)],
                                  ub = [1 for i in range(nseg)])

            w_vars = ['w_' + cs.id + "_%d" % i
                      for i in range(1, cs.value+1)]
            self.l_vars += w_vars

        ncat = len(self.cat)
        self.lp.variables.add(names = ["u_%d" % i for i in range(1, ncat)],
                              lb = [0 for i in range(ncat-1)],
                              ub = [1 for i in range(ncat-1)])

    def compute_constraint(self, aa, ap):
        c_vars = {}
        c_coefs = {}
        l_vars = []
        l_coefs = []
        for cs in self.cs:
            perf = ap.performances[cs.id]
            left = self.__get_left_points(cs.id, perf)
            d = self.points[cs.id][left + 1] - self.points[cs.id][left]
            k = (perf - self.points[cs.id][left]) / d

            w_coefs = [1] * left + [k] + [0] * (cs.value - left - 1)
            l_coefs += w_coefs

        return l_coefs

    def encode_constraint_cplex(self, aa, ap):
        constraints = self.lp.linear_constraints
        l_coefs = self.compute_constraint(aa, ap)

        cat_nr = self.cat[aa.category_id]

        if cat_nr < len(self.cat):
            constraints.add(names = ['csup' + aa.alternative_id],
                            lin_expr =
                                [[
                                 self.l_vars +
                                  ["u_%d" % cat_nr,
                                   'x_' + aa.alternative_id],
                                 l_coefs + [-1.0, 1.0],
                                ]],
                            senses = ["L"],
                            rhs = [-0.00001],
                           )

        if cat_nr > 1:
            constraints.add(names = ['cinf' + aa.alternative_id],
                            lin_expr =
                                [[
                                 self.l_vars +
                                  ["u_%d" % (cat_nr - 1),
                                   'y_' + aa.alternative_id],
                                 l_coefs + [-1.0, -1.0],
                                ]],
                            senses = ["G"],
                            rhs = [0.00001],
                           )

    def encode_constraints_cplex(self, aas, pt):
        self.add_variables_cplex(aas.keys())

        # sum ((sum w_it) + k * w_it+1) - u_k + x_j <= -d1
        # sum ((sum w_it) + k * w_it+1) - u_k - y_j >= d2
        for aa in aas:
            self.encode_constraint_cplex(aa, pt[aa.alternative_id])

        # sum (sum w_it) = 1
        constraints = self.lp.linear_constraints
        w = []
        for cs in self.cs:
            w += ['w_' + cs.id + "_%d" % (i + 1) for i in range(cs.value)]

        constraints.add(names = ['csum'],
                        lin_expr = [[w, [1] * len(w)]],
                        senses = ["E"],
                        rhs = [1],
                       )

        # u_k - u_k-1 >= s
        ncat = len(self.cat)
        for i in range(2, ncat):
            constraints.add(names = ["umin_%d_%d" % (i, i-1)],
                            lin_expr = [[
                                         ["u_%d" % i, "u_%d" % (i-1)],
                                         [1, -1],
                                       ]],
                            senses = ["G"],
                            rhs = [0.01],
                           )

    def add_objective_cplex(self, aa):
        self.lp.objective.set_sense(self.lp.objective.sense.minimize)
        for aa in aa.keys():
            self.lp.objective.set_linear('x_' + aa, 1)
            self.lp.objective.set_linear('y_' + aa, 1)

    def encode_constraints(self, aa, pt):
        if solver == 'cplex':
            self.encode_constraints_cplex(aa, pt)

    def add_objective(self, aa):
        if solver == 'cplex':
            self.add_objective_cplex(aa)

    def solve(self, aa, pt):
        self.encode_constraints(aa, pt)
        self.add_objective(aa)

        if solver == 'cplex':
            self.lp.solve()

        cfs = criteria_functions()
        cvs = criteria_values()
        for cs in self.cs:
            cv = criterion_value(cs.id, 1)
            cvs.append(cv)

            p1 = point(self.points[cs.id][0], 0)

            ui = 0
            f = piecewise_linear([])
            for i in range(cs.value):
                uivar = 'w_' + cs.id + "_%d" % (i + 1)
                ui += self.lp.solution.get_values(uivar)
                p2 = point(self.points[cs.id][i + 1], ui)

                s = segment(p1, p2)
                f.append(s)

                p1 = p2

            s.ph_in = True
            cf = criterion_function(cs.id, f)
            cfs.append(cf)

        cat = {v: k for k, v in self.cat.items()}
        catv = categories_values()
        ui_a = 0
        for i in range(1, len(cat)):
            ui_b = self.lp.solution.get_values("u_%d" % i)
            catv.append(category_value(cat[i], interval(ui_a, ui_b)))
            ui_a = ui_b

        catv.append(category_value(cat[i + 1], interval(ui_a, 1)))

        return cvs, cfs, catv

if __name__ == "__main__":
    from mcda.types import criteria_values, criterion_value
    from mcda.types import alternative_performances
    from mcda.types import criteria_functions, criterion_function
    from mcda.types import category_value, categories_values
    from mcda.types import interval
    from mcda.uta import utadis
    from tools.utils import normalize_criteria_weights
    from tools.utils import compute_ac
    from tools.generate_random import generate_random_alternatives
    from tools.generate_random import generate_random_categories
    from tools.generate_random import generate_random_criteria
    from tools.generate_random import generate_random_criteria_values
    from tools.generate_random import generate_random_performance_table
    from tools.generate_random import generate_random_criteria_functions

    # Generate an utadis model
    c = generate_random_criteria(10)
    cv = generate_random_criteria_values(c, seed = 1235)
    normalize_criteria_weights(cv)
    cat = generate_random_categories(4)

    cfs = generate_random_criteria_functions(c)

    catv1 = category_value("cat1", interval(0, 0.25))
    catv2 = category_value("cat2", interval(0.25, 0.65))
    catv3 = category_value("cat3", interval(0.65, 1))
    catv = categories_values([catv1, catv2, catv3])

    u = utadis(c, cv, cfs, catv)

    # Generate random alternative and compute assignments
    a = generate_random_alternatives(1000)
    pt = generate_random_performance_table(a, c)
    aa = u.get_assignments(pt)

    print('Original model')
    print('==============')
    print("Number of alternatives: %d" % len(a))

    # Learn the parameters from assignment examples
    gi_worst = alternative_performances('worst', {crit.id: 0 for crit in c})
    gi_best = alternative_performances('best', {crit.id: 1 for crit in c})

    css = criteria_values([])
    for cf in cfs:
        cs = criterion_value(cf.id, len(cf.function))
        css.append(cs)

    lp = lp_utadis(css, cat, gi_worst, gi_best)
    cvs, cfs, catv = lp.solve(aa, pt)

    u2 = utadis(c, cvs, cfs, catv)
    aa2 = u2.get_assignments(pt)

    print compute_ac(aa, aa2)
