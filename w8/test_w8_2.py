#!/bin/python
import pytest
from w8_2 import fib_generator

def fibonacci(n):
    if n == 0 :
        return 0
    elif n == 1 :
        return 1
    else :
        return fibonacci(n-1) + fibonacci(n-2)

def func_fib(n):
    A=[]
    for i in range(n):
        A.append(fibonacci(i))
    return A

def generator_array(n):
    A = [i for i in fib_generator(n)]
    return A

@pytest.mark.parametrize('num',[(2),(0),(1),(23)])
def test_fib_generator(num):
    assert generator_array(num) == func_fib(num)
