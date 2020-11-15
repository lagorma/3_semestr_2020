#!/bin/python
import numpy as np


class PrintAverage(Exception):
    pass

class PrintDispersion(Exception):
    pass

class PrintNumber(Exception):
    pass

def coroutine():
    print('Starting coroutine')
    A = []
    try:
        while True:
            try:
                x = yield
                A.append(x)
                average = np.mean(A)
                dispersion = np.var(A)
                n = len(A)
            except PrintDispersion:
                yield dispersion
            except PrintAverage:
                yield average
            except PrintNumber:
                yield n
    finally:
        print("Stop coroutine")

our_coroutine = coroutine()
next(our_coroutine)
for i in range(12):
    our_coroutine.send(i)
    if i%2 == 0:
        print("Average:", our_coroutine.throw(PrintAverage))
        next(our_coroutine)
    if i%3 == 0:
        print("Dispersion:", our_coroutine.throw(PrintDispersion))
        next(our_coroutine)
    if i%4 == 0:
        print("Number:", our_coroutine.throw(PrintNumber))
        next(our_coroutine)

print()
print(our_coroutine.throw(PrintAverage))
next(our_coroutine)

print(our_coroutine.throw(PrintDispersion))
next(our_coroutine)

print(our_coroutine.throw(PrintNumber))
next(our_coroutine)

our_coroutine.close()

