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
                return (math.sqrt(-x), 'i')
            else:
                return math.sqrt(x)
        except ValueError:
            return "Возникла ошибка, введите корректное число"





class MyComplexMath(MyMath):

    @classmethod
    def _complex(cls):
        return True


print(MyComplexMath.sqrt(-25))
print(MyMath.sqrt(-25))

'''
1) Инкапсуляция - каждое действие описано отдельной функцией
Полиморфизм - класс MyMath подразумевает ввод неверного числа (выводится ошибка)
Наследование - класс MyComplexMath копирует все методы MyMath и добавляет свой (переопределяет существуйющий)
2) Мы использовали классовый метод, так как вывод метода _complex зависит от того, в каком классе мы вызываем его
'''
