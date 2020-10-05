class NegativeNumber(Exception):
    pass
number=-1
if number < 0:
    raise NegativeNumber('Вы ввели отрицательное число')
