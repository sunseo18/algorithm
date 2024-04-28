import sys

n = int(sys.stdin.readline().strip())

MAX = 1001

array = [0] * MAX

array[1] = 1
array[2] = 3

for i in range(3, MAX):
    array[i] = ((array[i-2] * 2) + array[i-1]) % 10007

print(array[n])


