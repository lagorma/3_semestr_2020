#!/bin/python
from itertools import combinations

def get_combinations(s, n):
    A=[]
    for k in range(1,n+1):
        S=[]
        for el in combinations(s,k):
            stroka=''
            el=list(el)
            el.sort()
            for elem in el:
                stroka+=elem
            S.append(stroka)
        S.sort()
        A+=S
    return A


'''
Test for get_combinations

a=get_combinations('cat', 2)
print(a) #['a', 'c', 't', 'ac', 'at', 'ct']
'''
