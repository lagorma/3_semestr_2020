#!/bin/python

import multiprocessing

def scalar(a,b):
    return a*b

v1=[0,1,27,10]
v2=[3,14,5,64]

pool = multiprocessing.Pool(processes=4)
results = [pool.apply(scalar,args = (i,j)) for i,j in zip(v1,v2)]
print(sum(results))
