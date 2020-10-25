#!/bin/python

class Complex:


    def __init__(self, x, y): #x- действительная часть числа, у - мнимая
        self.x = x
        self.y = y


    def __add__(self, other):
        return Complex(self.x + other.x,self.y + other.y)


    def __sub__(self, other):
        return Complex(self.x-other.x,self.y-other.y)


    def __truediv__(self, other):
        a = (self.x * other.x + self.y * other.y)/(other.x ** 2 + other.y ** 2)
        b = (self.y * other.x - self.x * other.y)/(other.x ** 2 + other.y ** 2)
        return Complex(a,b)


    def __mul__(self, other):
        a = self.x * other.x - self.y * other.y
        b = self.y * other.x + self.x * other.y
        return Complex(a,b)


    def __pow__(self,other):
        a = self.x
        b = self.y
        step=other.x
        for _ in range (step-1):
            t=a
            o=b
            a = self.x * t - self.y * o
            b = o * self.x + t * self.y
        return Complex(a,b)


    def __abs__(self):
        return (self.x**2+self.y**2)**0.5

    def __neg__(self):
        a = - self.x
        b = - self.y
        return Complex(a,b)


    def __str__(self):
        if self.y == 0:
            return '{}'.format(self.x)
        elif self.y<0:
            return '{}{}i'.format(self.x,self.y)
        return '{}+{}i'.format(self.x,self.y)


a=Complex(1,2)
b=Complex(3,7)
r=Complex(3,0)

print(a+b) #4+9i
print(b-a) #2+5i
print(a-b) #-2-5i
print(a/b) #0,2931... - 0,01724...i
print(a*b) #-11+13i
print(a**r) #-11-2i
print(-a) #-1-2i
print(abs(a)) #2,23607...




