#!/bin/python
from itertools import combinations_with_replacement

def get_combinations_with_r(s, n):
    A=[]
    for el in combinations_with_replacement(s,n):
        el =list(el)
        el.sort()
        stroka=''
        for i in range(n):
            stroka+=el[i]
        A.append(stroka)
    A.sort()
    return A

'''
Test for get_combinations_with_r

a = get_combinations_with_r('cat', 2)
print(a) #['aa', 'ac', 'at', 'cc', 'ct', 'tt']
'''
