import sys

n = int(sys.stdin.readline().strip())

array = list(map(int, sys.stdin.readline().strip().split()))



array.sort()

sum = array[0]

for i in range(1, n):
    array[i] += array[i-1]

    sum += array[i]

print(sum)


