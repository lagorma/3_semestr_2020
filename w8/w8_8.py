#!/bin/python
from itertools import groupby

def isint(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def compress_string(s):
    A=[]
    for el in groupby(s):
        el = list(el)
        num=el[0]
        su=0
        while len(s)!=0 and s[0] == num:
            su+=1
            s=s[1::]
        el[1],el[0] = el[0],su
        if isint(el[1]):
            el[1] = int(el[1])
        el=tuple(el)
        A.append(el)
    return A

'''
Test for compress_string()

a=compress_string('1222311')
print(a)
'''
