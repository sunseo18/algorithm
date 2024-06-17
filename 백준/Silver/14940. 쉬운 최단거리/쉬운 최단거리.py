import sys
from collections import deque

n, m = map(int, sys.stdin.readline().strip().split())


di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

array = []

for i in range(n):
    array.append(list(sys.stdin.readline().strip().split()))


for i in range(n):
    for j in range(m):
        if array[i][j] == '1':
            array[i][j] = -1
        elif array[i][j] == '2':
            array[i][j] = 0
            end_i, end_j = i, j
        elif array[i][j] == '0':
            array[i][j] = 0
            
queue = deque([(end_i, end_j, 0)])


while queue:
    ci, cj, cd = queue.popleft()

    for i in range(4):
        ni, nj, nd = ci+di[i], cj+dj[i], cd + 1

        if 0 <= ni < n and 0 <= nj < m and array[ni][nj] == -1:
            array[ni][nj] = nd
            queue.append((ni, nj, nd))

for i in range(n):
    for j in range(m):
        sys.stdout.write(str(array[i][j]) + ' ')
    sys.stdout.write('\n')

            
