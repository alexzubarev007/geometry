import unittest
import math
from triangle import area, perimeter


class TriangleTestCase(unittest.TestCase):
    def test_integer_area(self):
        res = area(10, 3)
        self.assertEqual(res, 15)

    def test_rational_area(self):
        res = area(2, 1.5)
        self.assertEqual(res, 1.5)

    def test_invalid_area(self):
        self.assertRaises(Exception, lambda: area(-7, 5))

    def test_integer_perimeter(self):
        res = perimeter(5, 6, 7)
        self.assertEqual(res, 18)

    def test_rational_perimeter(self):
        res = perimeter(1.5, 2.7, 2.9)
        self.assertEqual(res, 7.1)

    def test_triangle_inequivalcy_perimeter(self):
        self.assertRaises(Exception, lambda: perimeter(1, 6, 9))

    def test_invalid_perimeter(self):
        self.assertRaises(Exception, lambda: perimeter(-1, 4, -5))