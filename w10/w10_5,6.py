#!/bin/python
import threading
import time
from matplotlib import pyplot as plt

#№5

a=0
def multiply(v1, v2):
    global a
    res = v1*v2
    lock.acquire()
    a+=res
    lock.release()

def run_threads(counter,v1,v2):
    threads = [threading.Thread(target=multiply, args = (v1[i],v2[i])) for i in range(0,counter)]
    for thread in threads:
        thread.start()

lock = threading.Lock()

v1 = [47747474847474744757,3839208384,108888888656654345,394948484585,3023454647,9990990840490444]
v2 = [575858803030303058558,93920848595749,3845775588973,9485589476585,83557583665,199999469697675656]
n = len(v1)

start_time = time.time()
run_threads(n,v1,v2)
finish_time = time.time()
time_prog = finish_time - start_time

print ('Finished. Scalar production is: {}. Runtime is: {}.'.format(a,round(time_prog,10)))


#№6
def scalar(v1,v2):
    a=0
    for i in range(len(v1)):
        res = v1[i]*v2[i]
        a+=res
    return a

number_of_threads = [1,1,1,3,3,3]
time1=[]
for k in range(3):
    start_time1 = time.time()
    scalar(v1,v2)
    finish1 = time.time() - start_time1
    time1.append(finish1)

for k in range(3):
    start_time = time.time()
    run_threads(n,v1,v2)
    finish_time = time.time()
    time_prog = finish_time - start_time
    time1.append(time_prog)

print(time1)

plt.plot(time1,number_of_threads)
plt.grid(True)
plt.show()
