#!/bin/python

class Shape:
    def width():
        a=float(input('Введите ширину: '))
        return a
    def length():
        b=float(input('Введите длину: '))
        return b

class Triangle(Shape):
    a=Shape.width()
    b=Shape.length()
    def area(a,b):
        return 0,5*a*b
    

class Rectangle(Shape):
    a=Shape.width()
    b=Shape.length()
    def area(a,b):
        return a*b
