#!/bin/python

'''
def print_map(function, iterable):
    for i in iterable:
        print(function(i))

Требуется переписать данную функцию не используя цикл for.
'''

def print_map(function, iterable):
    while next(iterable):
        print(function(next(iterable))




