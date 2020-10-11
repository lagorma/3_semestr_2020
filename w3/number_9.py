
k=input()
try:
   k= int(k)
except ValueError:
    print('Это не число')
finally:
    print('hello')
