import sys
from collections import deque

n, m = map(int, sys.stdin.readline().strip().split())

array = []
visited = [[False for _ in range(m)] for _ in range(n)]

for _ in range(n):
    array.append(list(sys.stdin.readline().strip()))

queue = deque()
for i in range(n):
    for j in range(m):
        if array[i][j] == 'I':
            queue.append((i, j, 0))
            visited[i][j] = True

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

answer = 0
while queue:
    ci, cj, depth = queue.popleft()

    if array[ci][cj] == 'P':
        answer += 1
        
    for d in range(4):
        ni, nj = ci + di[d], cj + dj[d]

        if 0 <= ni < n and 0 <= nj < m and array[ni][nj] != 'X' and not visited[ni][nj] :
            visited[ni][nj] = True
            queue.append((ni, nj, depth + 1))
            
if answer != 0:
    print(answer)
else:
    print('TT')
