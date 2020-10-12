#!/bin/python
def decorate(function):
    def the_wrapper(inlist):
        c=my_func(inlist)
        if c==0:
            return('Нет')
        elif c>10:
            return('Очень много')
        else:
            return c
    return the_wrapper


def my_func(A):
    c=0
    for el in A:
        if el%2==0:
            c+=1
    return c

print('Без декоратора')
print(my_func([1,3,4,6,7,0]))
print(my_func([1,3,5]))
print(my_func([2,4,6,8,10,12,14,16,18,20,22,24]))
my_func_2=decorate(my_func)
print('С декоратором')
print(my_func_2([1,3,4,6,7,0]))
print(my_func_2([1,3,5]))
print(my_func_2([2,4,6,8,10,12,14,16,18,20,22,24]))
