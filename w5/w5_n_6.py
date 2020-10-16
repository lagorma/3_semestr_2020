#!/bin/python

class Animal:
    __name = "unknown"
    __age = "unknown"

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def __str__(self):
        return self.get_str()


class Zebra(Animal):
    __type_of_zebra = 'unknown'

    def __init__(self, name, age, type_of_zebra):
        super().__init__(name, age)
        self.__type_of_zebra = type_of_zebra

    def get_type(self):
        return self.__type_of_zebra

    def get_str(self):
        return f"Имя: {self.get_name()}; Возраст: {self.get_age()}; Вид: {self.get_type()}"


class Dolphin(Animal):
    __color_of_Dolfin='unknown'

    def __init__(self, name, age, color_of_Dolfin):
        super().__init__(name, age)
        self.__color_of_Dolfin = color_of_Dolfin

    def get_color(self):
        return self.__color_of_Dolfin

    def get_str(self):
        return f"Имя: {self.get_name()}; Возраст: {self.get_age()}; Цвет: {self.get_color()}"

if __name__=="__main__":
    z = Zebra("Mary", "10", type_of_zebra='Equus quagga')
    d = Dolphin("Jonny", "2",color_of_Dolfin='grey')
    print(z)
    print(d)
