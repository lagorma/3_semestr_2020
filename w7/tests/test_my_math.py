#!/bin/python

import math
from my_mathematics.math import MyMath
from my_mathematics.linear_algebra import Vector
from my_mathematics.math import MyComplexMath
import cmath
import numpy as np



def test_sin():
    assert MyMath.sin(2) == math.sin(2)
    assert MyMath.sin(-12) == math.sin(-12)
    assert MyMath.sin(0) == math.sin(0)

def test_pi():
    assert MyMath.pi() == 3.14

def test_sqrt():
    assert MyMath.sqrt(4) == 2
    assert MyMath.sqrt(2.22) == math.sqrt(2.22)
    assert str(MyComplexMath.sqrt(-10)) == str(cmath.sqrt(-10))

def test_Vector():
    numpy_array_1 = np.array([40, 50, 60])
    numpy_array_2 = np.array([10, 20, 30])
    vect1=Vector('40,50,60')
    vect2=Vector('10,20,30')

    a=str(numpy_array_1+numpy_array_2)
    assert str(vect1+vect2) == ','.join([a[1:3],a[4:6],a[7:9]])

    a=str(numpy_array_1-numpy_array_2)
    assert str(vect1-vect2) == ','.join([a[1:3],a[4:6],a[7:9]])

    assert vect1*vect2 == np.sum(numpy_array_1*numpy_array_2)

    a=str(np.cross(numpy_array_1,numpy_array_2))
    a=list(a[2:-1].split(' '))
    a=list(el for el in a if el!='')
    assert str(vect1&vect2) == ','.join(a)


