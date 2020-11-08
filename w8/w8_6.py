#!/bin/python
from itertools import combinations

def get_combinations(s, n):
    try:
        A=[]
        for k in range(1,n+1):
            S=[]
            a=list(combinations(s,k))
            for el in a:
                stroka=''
                el=list(el)
                el.sort()
                for elem in el:
                    stroka+=elem
                S.append(stroka)
            S.sort()
            A+=S
        return A
    except:
        raise RuntimeError("Not implemented")


'''
Test for get_combinations

a=get_combinations('cat', 2)
print(a) #['a', 'c', 't', 'ac', 'at', 'ct']
'''
