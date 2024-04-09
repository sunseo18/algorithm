import sys
from itertools import combinations

def bigger(xy, pq):
    x, y = xy
    p, q = pq

    if x > p and y > q:
        return True
    
    return False

n = int(sys.stdin.readline().strip())

sizeList = []
for i in range(n):
    x, y = map(int, sys.stdin.readline().strip().split())

    sizeList.append((x, y))


for i in range(n):
    tmp = 0
    for j in range(n):
        if j == i:
            continue
        if bigger(sizeList[j], sizeList[i]):
            tmp += 1

    sys.stdout.write(str(tmp+1))
    sys.stdout.write(' ')
