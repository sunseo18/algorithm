import sys

n = int(sys.stdin.readline().strip())

array = []

for i in range(n):
    array.append(list(map(int, sys.stdin.readline().strip().split())))

for i in range(1, n):
    for j in range(3):
        tmp = []
        for k in range(3):
            if k != j:
                tmp.append(array[i-1][k] + array[i][j])
        array[i][j] = min(tmp)

print(min(array[n-1]))
