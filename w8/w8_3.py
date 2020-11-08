#!/bin/python

def copy_zip(a):

    len_a = len(a)

    min_len = float('inf')
    for i in range(len(a)):
        if min_len > len(a[i]):
            min_len = len(a[i])
    #print(min_len)

    s = 0
    while s < min_len:
        A=[]
        for i in range(len_a):
            #print(a[i][s])
            A.append(a[i][s])
        yield tuple(A)
        s += 1
'''
Test for copy_zip

a = [1,2,3]
b = "xyz"
c = (None, True)

res = list(copy_zip([a, b, c]))
print (res) #[(1, 'x', None), (2, 'y', True)]
'''

def copy_map(func,a):
    for i in range(len(a)):
        a[i] = func(a[i])
    return a

'''
Test for copy_map

old_list = ['1', '2', '3', '4', '5', '6', '7']
new_list = copy_map(int,old_list)
print(new_list)  #[1, 2, 3, 4, 5, 6, 7]
'''

def copy_enumerate(a):
    for i in range(len(a)):
        yield (i,a[i])


'''
Test for copy_enumerate

a = [10, 20, 30, 40]
A=[i for i in copy_enumerate(a)]
print(A) #[(0, 10), (1, 20), (2, 30), (3, 40)]

'''
