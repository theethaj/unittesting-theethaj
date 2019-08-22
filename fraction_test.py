import math
import time
import unittest
from fraction import Fraction


class FractionTest(unittest.TestCase):
    """Test the methods and constructor of the Fraction class. """

    def test_str(self):
        f = Fraction(3, -1)
        self.assertEqual("-3", f.__str__())
        f = Fraction(0, 5)
        self.assertEqual("0", f.__str__())
        f = Fraction(60, 90)
        self.assertEqual("2/3", f.__str__())
        f = Fraction(1500, 60)
        self.assertEqual("25", f.__str__())
        f = Fraction(1500, 90)
        self.assertEqual("50/3", f.__str__())
        f = Fraction(-80, 20)
        self.assertEqual("-4", f.__str__())
        f = Fraction(36, -60)
        self.assertEqual("-3/5", f.__str__())
        # Constructor should provide default denominator = 1
        f = Fraction(99)
        self.assertEqual("99", f.__str__())

    def test_add(self):
        # 3/4 = 2/3 + 1/12
        self.assertEqual(Fraction(3,4), Fraction(1,12)+Fraction(2,3))
        # 3/2 = 3/3 + 6/12
        self.assertEqual(Fraction(3,2), Fraction(3,3)+Fraction(6,12))
        # 11/15 = 2/5 + 5/15
        self.assertEqual(Fraction(11,15), Fraction(2,5)+Fraction(5,15))

    def test_eq(self):
        f = Fraction(1,0)
        g = Fraction(40,0)
        h = Fraction(10000,20001)       # not quite 1/2
        i = Fraction(-23,0)
        self.assertTrue(f == g)
        self.assertTrue(f.__eq__(g))    # same thing
        self.assertFalse(f == h)
        self.assertFalse(f.__eq__(h))
        self.assertFalse(g.__eq__(h))
        self.assertFalse(i.__eq__(f))