import sys
sys.path.insert(0, "..")
from mcda.uta import uta
from mcda.types import *
import unittest

class tests_uta(unittest.TestCase):

    def generate_model(self):
        c1 = criterion("c1")
        c2 = criterion("c2")
        c3 = criterion("c3")
        c = criteria([c1, c2, c3])

        cv1 = criterion_value("c1", 0.5)
        cv2 = criterion_value("c2", 0.25)
        cv3 = criterion_value("c3", 0.25)
        cvs = criteria_values([cv1, cv2, cv3])

        f1 = piecewise_linear([segment(point(0, 0), point(2.5, 0.2)),
                               segment(point(2.5, 0.2), point(5, 1), True,
                                                              True)])
        f2 = piecewise_linear([segment(point(0, 0), point(2.5, 0.8)),
                               segment(point(2.5, 0.8), point(5, 1), True,
                                                              True)])
        f3 = piecewise_linear([segment(point(0, 0), point(2.5, 0.5)),
                               segment(point(2.5, 0.5), point(5, 1), True,
                                                              True)])
        cf1 = criterion_function("c1", f1)
        cf2 = criterion_function("c2", f2)
        cf3 = criterion_function("c3", f3)
        cfs = criterion_functions([cf1, cf2, cf3])

        return uta(c, cvs, cfs)

    def test001(self):
        model = self.generate_model()

        a1 = alternative("a1")
        ap1 = alternative_performances("a1",
                                       {"c1": 2.5, "c2": 2.5, "c3": 2.5})
        a2 = alternative("a2")
        ap2 = alternative_performances("a1",
                                       {"c1": 5, "c2": 5, "c3": 5})
        a3 = alternative("a3")
        ap3 = alternative_performances("a3",
                                       {"c1": 0, "c2": 0, "c3": 0})

        self.assertAlmostEqual(model.global_utility(ap1).value, 0.425)
        self.assertAlmostEqual(model.global_utility(ap2).value, 1)
        self.assertAlmostEqual(model.global_utility(ap3).value, 0)

if __name__ == "__main__":
    suite = []
    suite.append(unittest.TestLoader().loadTestsFromTestCase(tests_uta))
    alltests = unittest.TestSuite(suite)
    unittest.TextTestRunner(verbosity=2).run(alltests)
