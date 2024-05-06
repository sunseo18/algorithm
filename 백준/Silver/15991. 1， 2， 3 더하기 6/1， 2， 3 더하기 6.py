import sys
from collections import deque

T = int(sys.stdin.readline().strip())


array = [1] * 100001

array[1] = 1
array[2] = 2
array[3] = 2
array[4] = 3
array[5] = 3
array[6] = 6
for i in range(7, 100001):
    array[i] = (array[i-2] + array[i-4] + array[i-6]) % 1000000009

for i in range(T):
    n = int(sys.stdin.readline().strip())

    sys.stdout.write(str(array[n]))
    sys.stdout.write('\n')
    
