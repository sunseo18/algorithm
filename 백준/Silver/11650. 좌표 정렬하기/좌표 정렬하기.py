import sys

n = int(sys.stdin.readline())
lista = [0] * n
for i in range(n):
    lista[i] = (x, y) = tuple(map(int, sys.stdin.readline().split()))

for t in sorted(lista):
    print(t[0], t[1])