import unittest
import math
from rectangle import area, perimeter
class RectangleTestCase(unittest.TestCase):
    def test_integer_area(self):
        res = area(10, 5)
        self.assertEqual(res, 50)

    def test_rational_area(self):
        res = area(2, 1.4)
        self.assertEqual(res, 2.8)

    def test_invalid_area(self):
       self.assertRaises(Exception, lambda: area(-1, 10))

    def test_integer_perimeter(self):
        res = perimeter(5, 6)
        self.assertEqual(res, 22)

    def test_rational_perimeter(self):
       res = perimeter(1.5, 1.6)
       self.assertEqual(res, 6.2)

    def test_invalid_perimeter(self):
        self.assertRaises(Exception, lambda: perimeter(-1, 10))