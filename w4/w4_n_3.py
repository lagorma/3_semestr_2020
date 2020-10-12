#!/bin/python
import sys
import argparse

def createParser ():
    parser = argparse.ArgumentParser()
    parser.add_argument ('-n', nargs='?')
    return parser

def fib(n):
    if n==0 or n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)


if __name__ == '__main__':
    parser = createParser()
    namespase = parser.parse_args()

#    print (namespase.n)
    print (fib(int(namespase.n)))
