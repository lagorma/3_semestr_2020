#!/bin/python

def copy_zip(*a):
    k=0
    s = 0
    while s!=None:
        A=[]
        for i in a:
            A.append(i[s])
            if i[s] == i[-1]:
                k = None
        yield tuple(A)
        if k != None:
            s += 1
        else:
            s = None

'''
Test for copy_zip

a = [1,2,3]
b = "xyz"
c = (None, True)

res = list(copy_zip(a, b, c))
print (res) #[(1, 'x', None), (2, 'y', True)]
'''



def copy_map(func,a):
    for i in a:
        yield func(i)


'''
Test for copy_map

old_list = ['1', '2', '3', '4', '5', '6', '7']
new_list = list(copy_map(int,old_list))
print(new_list)  #[1, 2, 3, 4, 5, 6, 7]
'''

def copy_enumerate(a):
    s=0
    for i in a:
        yield (s,i)
        s+=1


'''
Test for copy_enumerate

a = [10, 20, 30, 40]
A=[i for i in copy_enumerate(a)]
print(A) #[(0, 10), (1, 20), (2, 30), (3, 40)]
'''
