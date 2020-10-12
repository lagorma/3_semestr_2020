#!/bin/python

def swap(func):
    def wrapper(*args, **kwargs):
        args = reversed(args)
        func(*args, **kwargs)
    return wrapper


@swap
def div(x, y, show=False):
    result = x / y
    if show:
        print(result)
    return result

div(2, 4, show=True)

