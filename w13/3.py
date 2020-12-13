#!/bin/python
import pickle
from collections import deque
import os

class Tree:

    def __init__(self,a):
        self.Tree = a


    def add(self,x):
        self.Tree.append(x)


    def find(self,x):
        for i in range(len(self.Tree)):
            if self.Tree[i] == x:
                return i
        print('Not found')



    def delete(self,x):
        index = self.find(x)
        if type(index) != str:
            self.Tree = self.Tree[:index]+self.Tree[index+1:]
        else:
            print('Not found')


    def print(self):
        print(sorted(self.Tree))


    def clear(self):
        self.Tree = []


    def dump(self):
        with open('memory_Tree.txt','wb') as f:
            p = pickle.dump(self.Tree,f)



def recognition(order,Tree):
    A = list(order.split())
    if A[0] == 'add':
        Tree.add(A[1])
    elif A[0] == 'find':
        Tree.find(A[1])
    elif A[0] == 'delete':
        Tree.delete(A[1])
    elif A[0] == 'print':
        Tree.print()
    elif A[0] == 'clear':
        Tree.clear()
    elif A[0] == 'dump':
        Tree.dump()
    else:
        print('Введите корректную команду')



if __name__ == "__main__":
    if os.stat('memory_Tree.txt').st_size != 0:
        try:
            with open('memory_Tree.txt','rb') as file:
                p = pickle.load(file)
        except:
            p=[]
    else:
        p=[]
    My_Tree = Tree(p)
    order = input('Введите команду:')
    while order!='exit':
        recognition(order,My_Tree)
        order = input('Введите команду:')
    print('Приходите снова!')
