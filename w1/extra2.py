A=set(input().split())
B=set(input().split())
P=A.intersection(B)
R=A.symmetric_difference(B)
O=A.union(B)

print('пересечение',P)
print('симметричная разность',R)
print('объединение',O)
print('Супер ответ: несколько выводов одного и того же множества может выдать элементы в разном порядке, так как множество - содержит неупорядоченные элементы')


