import unittest
def area(a):
    '''
        Возвращает квадрат десятичного числа.
                   Параметр:
                       a (float) : десятичное число

        Возвращаемое значение:
                       area (float): площадь квадрата со стороной a
    '''
    return a * a


def perimeter(a):
    '''
            Возвращает учетверённое десятичное число.
                       Параметр:
                           a (float) : десятичное число

            Возвращаемое значение:
                           perimeter (float): периметр квадрата со стороной a
    '''

    return 4 * a


class SquareTestCase(unittest.TestCase):
    def test_integer_area(self):
        res = area(8)
        self.assertEqual(res, 64)

    def test_rational_area(self):
        res = area(1.7)
        self.assertEqual(res, 2.89)

    def test_invalid_area(self):
        self.assertRaises(Exception, lambda: area(-3))

    def test_integer_perimeter(self):
        res = perimeter(7)
        self.assertEqual(res, 28)

    def test_rational_perimeter(self):
        res = perimeter(6.1)
        self.assertEqual(res, 24.4)

    def test_invalid_perimeter(self):
        self.assertRaises(Exception, lambda: perimeter(-1))