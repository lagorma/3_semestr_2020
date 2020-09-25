A=list(map(int,input().split()))
S=[]
while A!=[]:
    S.append(A[0]+A[-1])
    A=A[1:-1:]
print(S)
    
