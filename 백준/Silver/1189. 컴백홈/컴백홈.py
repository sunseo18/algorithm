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

visited = [[0 for _ in range(C)] for _ in range(R)]
visited[R-1][0] = 1
answer = 0

no = 0
flag = False
def dfs(map, cur_i, cur_j, visited):
    global no
    global flag

    if visited[cur_i][cur_j] > K:
        visited[cur_i][cur_j] = 0
        return

    # 목표 지점에 왔을 때
    if cur_i == 0 and cur_j == C-1:
        if visited[cur_i][cur_j] == K:
            no += 1
        visited[cur_i][cur_j] = 0
        return


    for i in range(4):
        next_i = cur_i + dy[i]
        next_j = cur_j + dx[i]
        if 0<=next_i<R and 0<=next_j<C and map[next_i][next_j] != 'T' and visited[next_i][next_j] == 0:
            visited[next_i][next_j] = visited[cur_i][cur_j] + 1
            dfs(map, next_i, next_j, visited)

    visited[cur_i][cur_j] = 0
    
dfs(map, R-1, 0, visited)

print(no)
