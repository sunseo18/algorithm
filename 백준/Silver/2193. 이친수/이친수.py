import sys

n = int(sys.stdin.readline().strip())

MAX = 91

array = [0 for _ in range(MAX)]

array[1] = 1
array[2] = 1

for i in range(3, MAX):
    array[i] = array[i-1] + array[i-2]

sys.stdout.write(str(array[n]))
