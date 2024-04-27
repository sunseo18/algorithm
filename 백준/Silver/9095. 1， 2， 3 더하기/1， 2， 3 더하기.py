import sys

array = [0] * 12

array[1] = 1
array[2] = 2
array[3] = 4

for i in range(4, 12):
    array[i] = array[i-2]+array[i-1]+array[i-3]

n = int(sys.stdin.readline().strip())

for i in range(n):
    t = int(sys.stdin.readline().strip())
    sys.stdout.write(str(array[t]))
    sys.stdout.write('\n')

