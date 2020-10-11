#!/bin/python
import argparse
import sys

def createParser ():
    parser = argparse.ArgumentParser()
    parser.add_argument ('-a','--show-all',action='store_true',default=False)
    parser.add_argument('-f','--file',type=argparse.FileType('w'),default=False)
    parser.add_argument('num')
    return parser

def IsPrime(b):
    d=2
    while d*d<=b and b%d!=0:
        d+=1
    return d*d>b


def l_o_Pr_num(k):
    A=[]
    s=0
    while (len(A)-1)!=k:
        #print(A)
        if IsPrime(s):
            A.append(s)
        s+=1
    return A

if __name__ == '__main__':
    parser = createParser()
    my_args=parser.parse_args()
    #print(my_args)

    A=l_o_Pr_num(int(my_args.num))
    if my_args.show_all:
        print (*A,sep=' ')
        if my_args.file:
            with open(my_args.file.name,'w') as out:
                for el in A:
                    out.write(str(el)+'\n')
    else:
        if my_args.file:
            with open(my_args.file.name,'w') as out:
                out.write(str(A[-1])+'\n')
