import sys

n, m = map(int, sys.stdin.readline().strip().split())

noList = []
noListLength = 0
dList = []
for i in range(n):
    noListLength += 1
    noList.append(int(sys.stdin.readline().strip()))

noList.sort()


for i in range(m):
    target = int(sys.stdin.readline().strip())

    start, end = 0, noListLength-1

    while start < end:
        mid = (start + end) // 2
            
        if noList[mid] < target:
            start = mid+1
            
        elif noList[mid] >= target:
            end = mid

    if noList[start] == target:
        sys.stdout.write(str(start))

    else:
        sys.stdout.write('-1')
    sys.stdout.write('\n')

