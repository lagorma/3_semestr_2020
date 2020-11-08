#!/bin/python

def fib_generator(n):
    s = 0
    fib_0 = 0 #предыдущее число
    fib_1 = 0 #текущее число
    while s!=n:
        yield fib_1
        if s == 0:
            fib_1 = 1
            fib_0 = 0
        else:
            fib_0, fib_1 = fib_1, fib_0 + fib_1
        s += 1




