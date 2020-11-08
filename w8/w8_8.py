#!/bin/python
from itertools import groupby

def isint(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def compress_string(s):
    try:
        a=list(groupby(s))
        for i in range(len(a)):
            a[i] = list(a[i])
            num=a[i][0]
            su=0
            while len(s)!=0 and s[0] == num:
                su+=1
                s=s[1::]
            a[i][1],a[i][0] = a[i][0],su
            if isint(a[i][1]):
                a[i][1] = int(a[i][1])
            a[i]=tuple(a[i])
        return a
    except:
        raise RuntimeError("Not implemented")

'''
Test for compress_string()

a=compress_string('1222311')
print(a)
'''
