from __future__ import division
import sys
sys.path.insert(0, "..")
import unittest
import time
import random
from itertools import product

from mcda.electre_tri import electre_tri
from tools.meta_electre_tri_global import heuristic_profiles
from tools.utils import get_best_alternative_performances
from tools.utils import get_worst_alternative_performances
from tools.utils import get_pc_of_wrong_assignment
from tools.generate_random import generate_random_alternatives
from tools.generate_random import generate_random_criteria
from tools.generate_random import generate_random_criteria_values
from tools.generate_random import generate_random_performance_table
from tools.generate_random import generate_random_categories
from tools.generate_random import generate_random_categories_profiles
from tools.utils import normalize_criteria_weights

seeds = [ 123, 456, 789, 12, 345, 678, 901, 234, 567, 890 ]
#seeds = [ 901 ]

class heuristic_profiles_tests(unittest.TestCase):

    def variable_number_alternatives_and_criteria(self, ncat):
#        n_alts = [ i*100 for i in range(1, 11) ]
#        n_alts.extend([ i*1000 for i in range(1, 11) ])
#        n_crit = [ i for i in range(2,21) ]
        n_alts = [ 100 ]
        n_crit = [ 1 ]

        print ''
        nloop = { nc: {na: dict() for na in n_alts} for nc in n_crit }
        errors = { nc: {na: dict() for na in n_alts} for nc in n_crit }
        for nc, na, seed in product(n_crit, n_alts, seeds):
            a = generate_random_alternatives(na)
            c = generate_random_criteria(nc)
            cv = generate_random_criteria_values(c, seed)
            normalize_criteria_weights(cv)
            pt = generate_random_performance_table(a, c)

            b = generate_random_alternatives(ncat-1, 'b')
            bpt = generate_random_categories_profiles(b, c)
            cat = generate_random_categories(ncat)

            lbda = random.uniform(0.5, 1)

            model = electre_tri(c, cv, bpt, lbda, cat)
            aa = model.pessimist(pt)

            model.profiles.display()

            b0 = get_worst_alternative_performances(pt, c)
            bp = get_best_alternative_performances(pt, c)

            for j in range(1):
                model.profiles = generate_random_categories_profiles(b, c)
                heur = heuristic_profiles(model, a, c, pt, aa, b0, bp)
                for k in range(100):
                    aa2 = model.pessimist(pt)
                    wrong = get_pc_of_wrong_assignment(aa, aa2)
                    if wrong == 0:
                        break;
                    heur.optimize(aa2)
                    model.profiles.display(header=None)

                aa_learned = model.pessimist(pt)

            total = len(a)
            nok = 0
            for alt in a:
                if aa(alt.id) != aa_learned(alt.id):
                    nok += 1

            nloop[nc][na][seed] = k
            errors[nc][na][seed] = nok/total

            print("%d\t%d\t%s\t%d\t%-6.5f" % (nc, na, seed, k, nok/total))

        print('Summary')
        print('========')
        print("nseeds: %d" % len(seeds))
        print('nc\tna\tnloop\terrors')
        for nc, na in product(n_crit, n_alts):
            n = sum(nloop[nc][na].values())/len(seeds)
            err = sum(errors[nc][na].values())/len(seeds)
            print("%d\t%d\t%d\t%-6.5f" % (nc, na, n, err))

    def test001_two_categories(self):
        self.variable_number_alternatives_and_criteria(3)

#    def test002_three_categories(self):
#        self.variable_number_alternatives_and_criteria(3)
#
#    def test003_four_categories(self):
#        self.variable_number_alternatives_and_criteria(4)

if __name__ == "__main__":
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(heuristic_profiles_tests)
    unittest.TextTestRunner(verbosity=2).run(suite)