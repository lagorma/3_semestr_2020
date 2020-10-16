#!/bin/python

class Shape:
    def __init__(self,width,length):
        self.width=width
        self.length=length


class Triangle(Shape):
    def area(self):
        return (self.width*self.length)/2

    

class Rectangle(Shape):
    def area(self):
        return self.width*self.length

if __name__=="__main__":
    t=Triangle(5,3)
    r=Rectangle(5,8)

    print(t.area())
    print(r.area())
