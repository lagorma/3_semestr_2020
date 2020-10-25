#!/bin/python

class Vector:

    def __init__(self, a):
        A=list(map(int,a.split(',')))
        self.x = A[0]
        self.y = A[1]
        self.z = A[2]


    def __add__(self, other):
        return Vector('{},{},{}'.format(self.x + other.x, self.y + other.y, self.z + other.z))


    def __sub__(self, other):
        return Vector('{},{},{}'.format(self.x - other.x, self.y - other.y, self.z - other.z))


    def __mul__(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z


    def __and__(self, other):
        return Vector('{},{},{}'.format(self.y*other.z - self.z*other.y,
                      self.z*other.x - self.x * other.z,
                      self.x * other.y - self.y * other.x))


    def dist(self):
        return round((self.x**2 + self.y**2 + self.z**2)**0.5, 2)


    def __str__(self):
        return f"Вектор с координатами {self.x,self.y,self.z}"


vect1=Vector('1,2,3')
vect2=Vector ('3,4,5')

print(vect1+vect2)  #(4,6,8)
print(vect1-vect2) #(-2,-2,-2)
print(vect1*vect2) #26
print(vect1 & vect2) #(-2,4,-2)

#num 8
print('№8')
maximum=float('-inf')
N=int(input('Введите количество точек: '))
for i in range(N):
    S=list(map(int,input('Введите координаты точки (x y z): ').split()))
    v=Vector('{},{},{}'.format(S[0],S[1],S[2]))
    distant=Vector.dist(v)
    if distant>=maximum:
        maximum = distant
        Ans=S
print ("Самая далекая точка c координатами: {} находится на расстоянии {}".format([*Ans],maximum))

