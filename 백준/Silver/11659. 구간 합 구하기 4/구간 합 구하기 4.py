import sys

array = []

n, m = map(int, sys.stdin.readline().strip().split())

array = list(map(int, sys.stdin.readline().strip().split()))

for i in range(1, n):
    array[i] += array[i-1]
    
for i in range(m):
    a, b = map(int, sys.stdin.readline().strip().split())
    i, j = a-1, b-1

    if i == 0:
        sys.stdout.write(str(array[j]))
    elif i == j:
        sys.stdout.write(str(array[j] - array[j-1]))
    else:
        sys.stdout.write(str(array[j] - array[i-1]))

    sys.stdout.write('\n')
