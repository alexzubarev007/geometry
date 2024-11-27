import unittest
import math
from circle import area, perimeter
class СircleTestCase(unittest.TestCase):
    def test_ten_area(self):
        res = area(10)
        self.assertEqual(res, 314.1592653589793)

    def test_one_divide_pi_area(self):
        res = area(1/(math.sqrt(math.pi)))
        self.assertAlmostEqual(res, 1, places = 2)

    def test_invalid_area(self):
       self.assertRaises(Exception, lambda: area(-1))

    def test_five_perimeter(self):
        res = perimeter(5)
        self.assertEqual(res, 31.41592653589793)

    def test_one_div_half_pi_perimeter(self):
       res = perimeter(1 / (2*math.pi))
       self.assertEqual(res, 1)

    def test_invalid_perimeter(self):
        self.assertRaises(Exception, lambda: perimeter(-1))



