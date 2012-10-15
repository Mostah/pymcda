import sys
sys.path.insert(0, "..")
from xml.etree import ElementTree
from lxml import etree
from mcda.types import *
import unittest

XMCDA_HEADER = '{http://www.decision-deck.org/2012/XMCDA-2.2.1}XMCDA'
XMCDA_FILE = 'XMCDA-2.2.1.xsd'

class tests_xmcda(unittest.TestCase):

    def validate(self, xml):
        root = ElementTree.Element(XMCDA_HEADER)
        root.append(xml)
        xml = ElementTree.tostring(root)

        doc = etree.parse(XMCDA_FILE)
        schema = etree.XMLSchema(doc)
        return schema.validate(etree.fromstring(xml))

    def test001(self):
        c1 = criterion("c1")
        c2 = criterion("c2")
        c = criteria([c1, c2])
        xmcda = c.to_xmcda()

        self.assertEqual(self.validate(xmcda), True)

        c_from = criteria().from_xmcda(xmcda)
        self.assertEqual(c, c_from)

    def test002(self):
        a1 = alternative("a1")
        a2 = alternative("a2")
        a = alternatives([a1, a2])
        xmcda = a.to_xmcda()

        self.assertEqual(self.validate(xmcda), True)

        a_from = alternatives().from_xmcda(xmcda)
        self.assertEqual(a, a_from)

    def test003(self):
        cv1 = criterion_value('c1', 10)
        cv2 = criterion_value('c2', 20)
        cv = criteria_values([cv1, cv2])
        xmcda = cv.to_xmcda()

        self.assertEqual(self.validate(xmcda), True)

        cv_from = criteria_values().from_xmcda(xmcda)
        self.assertEqual(cv, cv_from)

    def test004(self):
        p1 = alternative_performances('a1', {'c1': 120, 'c2':  284})
        p2 = alternative_performances('a2', {'c1': 150, 'c2':  269})
        pt = performance_table([p1, p2])
        xmcda = pt.to_xmcda()

        self.assertEqual(self.validate(xmcda), True)

        pt_from = performance_table().from_xmcda(xmcda)
        self.assertEqual(pt, pt_from)

    def test005(self):
        cv1 = category_value('cat1', interval(0, 0.25))
        cv2 = category_value('cat2', interval(0.25, 0.5))
        cv = categories_values([cv1, cv2])
        xmcda = cv.to_xmcda()

        self.assertEqual(self.validate(xmcda), True)

        cv_from = categories_values().from_xmcda(xmcda)
        self.assertEqual(cv, cv_from)

    def test006(self):
        av1 = alternative_value('a1', 10)
        av2 = alternative_value('a2', 20)
        av = alternatives_values([av1, av2])
        xmcda = av.to_xmcda()

        self.assertEqual(self.validate(xmcda), True)

        av_from = alternatives_values().from_xmcda(xmcda)
        self.assertEqual(av, av_from)

    def test007(self):
        af1 = alternative_affectation('a1', 'cat1')
        af2 = alternative_affectation('a2', 'cat2')
        af = alternatives_affectations([af1, af2])
        xmcda = af.to_xmcda()

        self.assertEqual(self.validate(xmcda), True)

    def test008(self):
        cp1 = category_profile('b1', limits('cat1', 'cat2'))
        cp2 = category_profile('b2', limits('cat2', 'cat3'))
        cp = categories_profiles([cp1, cp2])
        xmcda = cp.to_xmcda()

        self.assertEqual(self.validate(xmcda), True)

    def test009(self):
        cat1 = category('cat1', rank=1)
        cat2 = category('cat2', rank=2)
        cat = categories([cat1, cat2])
        xmcda = cat.to_xmcda()

        self.assertEqual(self.validate(xmcda), True)

class tests_segment(unittest.TestCase):

    def test001(self):
        p1 = point(0, 0)
        p2 = point(5, 5)
        s = segment(p1, p2)
        self.assertEqual(s.y(2), 2)

    def test002(self):
        p1 = point(0, 0)
        p2 = point(5, 5)
        s = segment(p1, p2)
        self.assertRaises(ValueError, s.y, -1)

    def test003(self):
        p1 = point(0, 0)
        p2 = point(5, 5)
        s = segment(p1, p2)
        self.assertRaises(ValueError, s.y, 6)

    def test004(self):
        p1 = point(0, 0)
        p2 = point(5, 5)
        s = segment(p1, p2)
        self.assertEquals(s.y(0), 0)

    def test005(self):
        p1 = point(0, 0)
        p2 = point(5, 5)
        s = segment(p1, p2, False)
        self.assertRaises(ValueError, s.y, 0)

    def test006(self):
        p1 = point(0, 0)
        p2 = point(5, 5)
        s = segment(p1, p2)
        self.assertRaises(ValueError, s.y, 5)

    def test007(self):
        p1 = point(0, 0)
        p2 = point(5, 5)
        s = segment(p1, p2, True, True)
        self.assertEquals(s.y(5), 5)

class tests_piecewise_linear(unittest.TestCase):

    def test001(self):
        p1 = point(0, 0)
        p2 = point(1, 1)
        s1 = segment(p1, p2)

        p3 = point(1, 5)
        p4 = point(5, 9)
        s2 = segment(p3, p4)

        plf = piecewise_linear([s1, s2])
        self.assertEquals(plf.y(3), 7)

    def test002(self):
        p1 = point(0, 0)
        p2 = point(1, 1)
        s1 = segment(p1, p2)

        p3 = point(1, 5)
        p4 = point(5, 9)
        s2 = segment(p3, p4)

        plf = piecewise_linear([s1, s2])
        self.assertEquals(plf.y(0.5), 0.5)

    def test003(self):
        p1 = point(0, 0)
        p2 = point(1, 1)
        s1 = segment(p1, p2)

        p3 = point(1, 5)
        p4 = point(5, 9)
        s2 = segment(p3, p4)

        plf = piecewise_linear([s1, s2])
        self.assertEquals(plf.y(0), 0)

    def test004(self):
        p1 = point(0, 0)
        p2 = point(1, 1)
        s1 = segment(p1, p2)

        p3 = point(1, 5)
        p4 = point(5, 9)
        s2 = segment(p3, p4)

        plf = piecewise_linear([s1, s2])
        self.assertEquals(plf.y(1), 5)

    def test005(self):
        p1 = point(0, 0)
        p2 = point(1, 1)
        s1 = segment(p1, p2)

        p3 = point(1, 5)
        p4 = point(5, 9)
        s2 = segment(p3, p4)

        plf = piecewise_linear([s1, s2])
        self.assertEquals(plf.y(0), 0)

    def test006(self):
        p1 = point(0, 0)
        p2 = point(1, 1)
        s1 = segment(p1, p2)

        p3 = point(1, 5)
        p4 = point(5, 9)
        s2 = segment(p3, p4)

        plf = piecewise_linear([s1, s2])
        self.assertRaises(ValueError, plf.y, 5)

    def test007(self):
        p1 = point(0, 0)
        p2 = point(1, 1)
        s1 = segment(p1, p2)

        p3 = point(3, 7)
        p4 = point(5, 9)
        s2 = segment(p3, p4)

        plf = piecewise_linear([s1, s2])
        self.assertRaises(ValueError, plf.y, 2)

    def test008(self):
        p1 = point(0, 0)
        p2 = point(1, 1)
        s1 = segment(p1, p2)

        p3 = point(3, 7)
        p4 = point(5, 9)
        s2 = segment(p3, p4)

        plf = piecewise_linear([s1, s2])
        self.assertRaises(ValueError, plf.y, 1)

if __name__ == "__main__":
    suite = []
    suite.append(unittest.TestLoader().loadTestsFromTestCase(tests_xmcda))
    suite.append(unittest.TestLoader().loadTestsFromTestCase(tests_segment))
    suite.append(unittest.TestLoader().loadTestsFromTestCase(tests_piecewise_linear))
    alltests = unittest.TestSuite(suite)
    unittest.TextTestRunner(verbosity=2).run(alltests)
