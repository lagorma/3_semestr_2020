#!/bin/python

class Mother:
    __name = "unknown"

    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_str(self):
        return f"Мама: {self.get_name()}"

    def __str__(self):
        return self.get_str()


class Daughter(Mother):
    __mother = "unknown"

    def __init__(self, name, mother):
        super().__init__(name)
        self.__mother = mother

    def get_mother(self):
        return self.__mother

    def set_mother(self, mother):
        self.__mother = mother

    def get_str(self):
        return f"Дочь: {self.get_name()}; Мама: {self.get_mother()}"

'''
if __name__=="__main__":
    m=Mother('Ольга')
    d=Daughter('Екатерина','Анфиса')

    print(m)
    print(d)
'''

