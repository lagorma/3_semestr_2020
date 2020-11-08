#!/bin/python
from itertools import permutations

def get_permutations(s, n):
    try:
        a=list(permutations(s,n))
        A=[]
        for i in range(len(a)):
            stroka=''
            for el in a[i]:
                stroka+=el
            A.append(stroka)
        A.sort()
        return A
    except:
        raise RuntimeError("Not implemented")

'''
Test for get_permutations

a=get_permutations('cat',2)
print(a)
'''
