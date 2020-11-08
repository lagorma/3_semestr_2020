#!/bin/python
from itertools import combinations_with_replacement

def get_combinations_with_r(s, n):
    try:
        A=[]
        a=list(combinations_with_replacement(s,n))
        for k in range(len(a)):
            a[k]=list(a[k])
            a[k].sort()
            stroka=''
            for i in range(n):
                stroka+=a[k][i]
            A.append(stroka)
        A.sort()
        return A
    except:
        raise RuntimeError("Not implemented")
'''
Test for get_combinations_with_r

a=get_combinations_with_r('cat', 2)
print(a)
'''
