import unittest
def area(a,b):
    '''
            Возвращает произведение двух десятичных чисел.
                       Параметры:
                           a (float) : десятичное число
                           b (float) : десятичное число

            Возвращаемое значение:
                           area (float): площадь прямоугольника со сторонами a и b
    '''
    return a*b

def perimeter(a,b):
    '''
                Возвращает удвоенную сумму двух десятичных чисел.
                           Параметры:
                               a (float) : десятичное число
                               b (float) : десятичное число

                Возвращаемое значение:
                               perimeter (float): периметр прямоугольника со сторонами a и b
        '''
    return (a+b)*2

class RectangleTestCase(unittest.TestCase):
    def test_sides_ten_five_area(self):
        res = area(10, 5)
        self.assertEqual(res, 50)

    def test_sides_two_one_and_half_area(self):
        res = area(2, 1.5)
        self.assertEqual(res, 3)

    def test_invalid_area(self):
       self.assertRaises(Exception, lambda: area(-1, 10))

    def test_sides_five_six_perimeter(self):
        res = perimeter(5, 6)
        self.assertEqual(res, 22)

    def test_sides_one_and_half_perimeter(self):
       res = perimeter(1.5, 1.5)
       self.assertEqual(res, 6)

    def test_invalid_perimeter(self):
        self.assertRaises(Exception, lambda: perimeter(-1, 10))