import sys
from collections import deque

n, m= map(int, sys.stdin.readline().strip().split())

maps = []
for i in range(n):
    maps.append(list(sys.stdin.readline().strip()))


queue = deque([(0, 0, 1)])


di = [0, 0, -1, 1]
dj = [-1, 1, 0, 0]

while queue:
    ci, cj, cd = queue.popleft()

    if ci == n-1 and cj == m-1:
        print(cd)
        
    for d in range(4):
        ni, nj = ci + di[d], cj + dj[d]

        if 0 <= ni < n and 0 <= nj < m and maps[ni][nj] != '0':
            maps[ni][nj] = '0'
            queue.append((ni, nj, cd+1))
