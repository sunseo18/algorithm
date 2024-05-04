import sys
from collections import deque

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
R, C, K = map(int, sys.stdin.readline().strip().split())

map = []
for i in range(R):
    map.append(list(sys.stdin.readline().strip()))


queue = deque()
queue.append([R-1, 0])

visited = [[False for _ in range(C)] for _ in range(R)]
answer = 0

no = 0
flag = False
def dfs(map, cur_i, cur_j, visited, depth):
    global no
    global flag

    if depth > K:
        return

    # 목표 지점에 왔을 때
    if cur_i == 0 and cur_j == C-1:
        if depth == K:
            no += 1
        return

    visited[cur_i][cur_j] = True

    for i in range(4):
        next_i = cur_i + dy[i]
        next_j = cur_j + dx[i]
        if 0<=next_i<R and 0<=next_j<C and map[next_i][next_j] != 'T' and not visited[next_i][next_j]:
            dfs(map, next_i, next_j, visited, depth + 1)

    visited[cur_i][cur_j] = False
    
dfs(map, R-1, 0, visited, 1)

print(no)
