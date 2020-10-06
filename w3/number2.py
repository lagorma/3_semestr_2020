#!/bin/python3

'''
def write_array(array,file_name):
    with open(array,'r') as input, open(file_name,'w') as output:
        output.write(input.read())
    pass
'''

def write_array(array,file_name):
    with open(file_name,'w') as my_file:
        for line in array:
            my_file.write(line+'\n')


my_array=['abc','cdf','ghi','jkl']
write_array(my_array,'output.txt')

