#!/bin/python
import math

class MyMath:


    def __init__(self, x):
        self.__x = x


    @staticmethod
    def sin(x):
        return math.sin(x)


    @staticmethod
    def pi():
        return 3.14


    @classmethod
    def _complex(cls):
        return False


    @classmethod
    def sqrt(cls, x):
        try:
            #print(cls._complex())
            if cls._complex():
                a=math.sqrt(-x)
                if a.is_integer():
                    a=int(a)
                return '{}j'.format(a)
            else:
                return math.sqrt(x)
        except ValueError:
            return "Возникла ошибка, введите корректное число"


class MyComplexMath(MyMath):

    @classmethod
    def _complex(cls):
        return True
