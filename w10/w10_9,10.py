#!/bin/python
import multiprocessing
import time
import matplotlib.pyplot as plt
from multiprocessing import Queue
import timeit

def multiply(c1, c2):
    return c1*c2

def creator(q,res):
    q.put(res)
    return q

a=0

def consumer(q,counter):
    global a
    for i in range(counter):
        res = q.get()
        a+=res
    return a

def run_processes(counter,v1,v2,q):
    processes = [multiprocessing.Process(target=creator, args = (q,multiply(v1[i],v2[i]))) for i in range(0,counter)]
    for process in processes:
        process.start()
    for process in processes:
        process.join()
    consumer(q,counter)

q = Queue()
v1 = [13838383838,238475646464646,3470873678236587265,52345681436578203648723965,123417568273642078365,53285673478561289756]
v2 = [3393994894853,448487575893303,5478327578264587345,425267384657846587464,842375682376520874567,62038754567445637845]
n = len(v1)
start_time = time.time()
run_processes(n,v1,v2,q)
finish_time = time.time()
time_prog = finish_time - start_time
print ('Finished. Scalar production is: {}. Runtime is: {}.'.format(a,round(time_prog,10)))

def scalar(v1,v2):
    b=0
    for i in range(len(v1)):
        res = v1[i]*v2[i]
        b+=res
    return b

number_of_processes = [1,1,1,3,3,3]
my_time=[]
for k in range(3):
    start_time = timeit.default_timer()
    scalar(v1,v2)
    finish_time = time.time()
    time_prog = finish_time - start_time
    my_time.append(time_prog)
for k in range(3):
    start_time = time.time()
    run_processes(n,v1,v2,q)
    finish_time = time.time()
    time_prog = finish_time - start_time
    my_time.append(time_prog)

#print(my_time,number_of_processes)
plt.plot(my_time,number_of_processes)
plt.grid(True)
plt.show()
