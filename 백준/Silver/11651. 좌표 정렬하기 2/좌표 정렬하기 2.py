import sys

n = int(sys.stdin.readline())
lista = [0] * n
for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    lista[i] = (y, x)

for t in sorted(lista):
    print(t[1], t[0])