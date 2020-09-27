#!/bin/python3

def write_array(array,file_name):
    with open(array,'r') as input, open(file_name,'w') as output:
        output.write(input.read())
    pass



write_array('input.txt','output.txt')
