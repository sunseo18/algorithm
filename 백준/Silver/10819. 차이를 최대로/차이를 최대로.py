import sys
from itertools import permutations

n = int(sys.stdin.readline().strip())
array = list(map(int, sys.stdin.readline().strip().split()))

indexArray = [i for i in range(0, n)]

indexPer = permutations(indexArray, n)

maxVal = -800
for indexes in indexPer:

    tmp = 0
    for i in range(0, n-1):
        tmp += abs(array[indexes[i]] - array[indexes[i+1]])
    maxVal = max(maxVal, tmp)
    
print(maxVal)
