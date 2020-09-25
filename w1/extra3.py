def izdevatelstvo(a,b=1000,c=100):
    return a+b+c
    

print('1)',izdevatelstvo(2,3,4))
print('2)',izdevatelstvo(4,c=3))
print('3)',izdevatelstvo(*[3,4,5]))
print('4)',izdevatelstvo(**{'a':1,'b':444442,'c':3}))






