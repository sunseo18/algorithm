import sys

n, q = map(int, sys.stdin.readline().strip().split())

nList = list(map(int, sys.stdin.readline().strip().split()))

nList.sort()

for i in range(1, n):
    nList[i] += nList[i-1]


for i in range(q):
    l, r = map(int, sys.stdin.readline().strip().split())
    l -= 1
    r -= 1
    
    if l == r:
        sys.stdout.write(str(nList[l] - nList[l-1]))

    
    elif l == 0:
        sys.stdout.write(str(nList[r]))

    else:
        sys.stdout.write(str(nList[r] - nList[l-1]))
        
    sys.stdout.write('\n')
