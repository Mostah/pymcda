from __future__ import division
import sys
sys.path.insert(0, "..")
import unittest
import time
import random
from itertools import product

from mcda.types import alternatives_affectations, performance_table
from mcda.electre_tri import electre_tri
from inference.lp_electre_tri_weights import lp_electre_tri_weights
from tools.generate_random import generate_random_alternatives
from tools.generate_random import generate_random_criteria
from tools.generate_random import generate_random_criteria_values
from tools.generate_random import generate_random_performance_table
from tools.generate_random import generate_random_categories
from tools.generate_random import generate_random_profiles
from tools.generate_random import generate_random_categories_profiles
from tools.utils import normalize_criteria_weights
from tools.utils import add_errors_in_affectations

seeds = [ 123, 456, 789, 12, 345, 678, 901, 234, 567, 890 ]

def variable_number_alternatives_and_criteria(ncat, er=0, nlearn=1.0):
    n_alts = [ i*1000 for i in range(1, 11) ]
    n_crit = [ i for i in range(2,21) ]
    n_alts = [ i*1000 for i in range(1, 11) ]
    n_crit = [ 5, 7, 10]

    print('\nnc\tna\tncat\tnlearn\terr\tseed\tobj\terrors\terr_bad'
          '\tt_total\tt_const\tt_solve')

    objectives = { nc: {na: dict() for na in n_alts} for nc in n_crit }
    times_total = { nc: {na: dict() for na in n_alts} for nc in n_crit }
    times_const = { nc: {na: dict() for na in n_alts} for nc in n_crit }
    times_solve = { nc: {na: dict() for na in n_alts} for nc in n_crit }
    errors = { nc: {na: dict() for na in n_alts} for nc in n_crit }
    errors_min = { nc: {na: dict() for na in n_alts} for nc in n_crit }
    errors_max = { nc: {na: dict() for na in n_alts} for nc in n_crit }
    errors_erroned = { nc: {na: dict() for na in n_alts} for nc in n_crit }
    for nc, na, seed in product(n_crit, n_alts, seeds):
        a = generate_random_alternatives(na)
        c = generate_random_criteria(nc)
        cv = generate_random_criteria_values(c, seed)
        normalize_criteria_weights(cv)
        pt = generate_random_performance_table(a, c)

        cat = generate_random_categories(ncat)
        cps = generate_random_categories_profiles(cat)
        b = cps.get_ordered_profiles()
        bpt = generate_random_profiles(b, c)

        lbda = random.uniform(0.5, 1)

        model = electre_tri(c, cv, bpt, lbda, cps)
        aa = model.pessimist(pt)

        a_learn = random.sample(a, int(nlearn*len(a)))
        aa_learn = alternatives_affectations([ aa[alt.id]
                                               for alt in a_learn ])
        pt_learn = performance_table([ pt[alt.id] for alt in a_learn ])

        aa_err = aa_learn.copy()
        aa_erroned = add_errors_in_affectations(aa_err, cat.get_ids(), er)

        t1 = time.time()
        lp_weights = lp_electre_tri_weights(model, pt_learn, aa_err, cps,
                                            0.0001)
        t2 = time.time()
        obj = lp_weights.solve()
        t3 = time.time()

        objectives[nc][na][seed] = obj
        times_total[nc][na][seed] = t3-t1
        times_const[nc][na][seed] = t2-t1
        times_solve[nc][na][seed] = t3-t2

        aa_learned = model.pessimist(pt)

        total = len(a)
        nok = nok_erroned = 0
        a_assign = { alt.alternative_id: alt.category_id for alt in aa }
        a_assign2 = { alt.alternative_id: alt.category_id
                      for alt in aa_learned}
        for alt in a:
            if a_assign[alt.id] != a_assign2[alt.id]:
                nok += 1
                if alt.id in aa_erroned:
                    nok_erroned += 1

        e = nok/total
        errors[nc][na][seed] = nok / total
        e_err = nok_erroned / total

        errors_erroned[nc][na][seed] = e_err

        print("%d\t%d\t%d\t%-6.4f\t%-6.4f\t%s\t%-6.4f\t%-6.5f\t%-6.5f"
              "\t%-6.5f\t%-6.5f\t%-6.5f" % (nc, na, ncat, nlearn, er, seed,
              obj, e, e_err, t3-t1, t2-t1, t3-t2))

    print('Summary')
    print('========')
    print("nseeds: %d" % len(seeds))
    print('nc\tna\tncat\tnlearn\terr\tobj\terr_avg\terr_min\terr_max' \
          '\terr_bad\tt_total\tt_cons\tt_solve')
    for nc, na in product(n_crit, n_alts):
        obj = sum(objectives[nc][na].values())/len(seeds)
        tim_tot = sum(times_total[nc][na].values())/len(seeds)
        tim_con = sum(times_const[nc][na].values())/len(seeds)
        tim_sol = sum(times_solve[nc][na].values())/len(seeds)
        err = sum(errors[nc][na].values())/len(seeds)
        err_min = min(errors[nc][na].values())
        err_max = max(errors[nc][na].values())
        err_erroned = sum(errors_erroned[nc][na].values())/len(seeds)
        print("%d\t%d\t%d\t%-6.5f\t%-6.5f\t%-6.4f\t%-6.5f\t%-6.5f\t%-6.5f"
              "\t%-6.5f\t%-6.5f\t%-6.5f\t%-6.5f" % (nc, na, ncat,
              nlearn, er, obj, err, err_min, err_max, err_erroned,
              tim_tot, tim_con, tim_sol))

class tests_lp_electre_tri_weights(unittest.TestCase):

    def test001_two_categories(self):
        variable_number_alternatives_and_criteria(2)

    def test002_three_categories(self):
        variable_number_alternatives_and_criteria(3)

    def test003_four_categories(self):
        variable_number_alternatives_and_criteria(4)

    def test004_five_categories(self):
        variable_number_alternatives_and_criteria(5)

class tests_lp_electre_tri_weights_with_errors(unittest.TestCase):

    def test001_two_categories_errors_10pc(self):
        variable_number_alternatives_and_criteria(2, 0.1)

    def test002_two_categories_errors_20pc(self):
        variable_number_alternatives_and_criteria(2, 0.2)

    def test003_two_categories_errors_30pc(self):
        variable_number_alternatives_and_criteria(2, 0.3)

    def test004_two_categories_errors_40pc(self):
        variable_number_alternatives_and_criteria(2, 0.4)

    def test005_three_categories_errors_10pc(self):
        variable_number_alternatives_and_criteria(3, 0.1)

    def test006_three_categories_errors_20pc(self):
        variable_number_alternatives_and_criteria(3, 0.2)

    def test007_three_categories_errors_30pc(self):
        variable_number_alternatives_and_criteria(3, 0.3)

    def test008_three_categories_errors_40pc(self):
        variable_number_alternatives_and_criteria(3, 0.4)

if __name__ == "__main__":
    loader = unittest.TestLoader()
    suite1 = loader.loadTestsFromTestCase(tests_lp_electre_tri_weights)
    suite2 = loader.loadTestsFromTestCase(tests_lp_electre_tri_weights_with_errors)
    alltests = unittest.TestSuite([suite1, suite2])
    unittest.TextTestRunner(verbosity=2).run(alltests)
