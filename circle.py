import math
import unittest

def area(r):
    '''
       Возвращает произведение квадрата десятичного числа и константы math.pi.
           Параметр:
               r (float) : десятичное число

       Возвращаемое значение:
               area (float): площадь круга с радиусом r
    '''
    return math.pi * r * r


def perimeter(r):
    '''
       Возвращает удвоенное произведение десятичного числа и константы math.pi.
           Параметр:
               r (float) : десятичное число

       Возвращаемое значение:
               perimeter (float): длина окружности радиусa r
       '''
    return 2 * math.pi * r

