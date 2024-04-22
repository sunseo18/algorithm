import sys
from itertools import permutations

n, m = map(int, input().split())

arr = [str(i) for i in range(1, n+1)]

permuList = list(permutations(arr, m))

for p in permuList:
    sys.stdout.write(" ".join(p))
    sys.stdout.write("\n")
