import sys
from collections import deque

m, n, h = map(int, sys.stdin.readline().strip().split())

h_direction = [0, 0, 0, 0, -1, 1]
n_direction = [0, -1, 0, 1, 0, 0]
m_direction = [1, 0, -1, 0, 0, 0]
tomatoes = []

for _ in range(h):
    tmp = []
    for _ in range(n):
        tmp.append(list(map(int, sys.stdin.readline().strip().split())))
    tomatoes.append(tmp)

visited = [[[-1 for _ in range(m)] for _ in range(n)] for _ in range(h)]
visited_max = 0
queue = deque()

for height in range(h):
    for i in range(n):
        for j in range(m):
            if tomatoes[height][i][j] == 1:
                queue.append((height, i, j))
                visited[height][i][j] = 0
        
while queue:
    cur = queue.popleft()
    
    for i in range(6):
        new_h = cur[0] + h_direction[i]
        new_n = cur[1] + n_direction[i]
        new_m = cur[2] + m_direction[i]

        if (h > new_h and new_h >= 0) and (n > new_n and new_n >= 0) and (m > new_m and new_m >= 0):
            if visited[new_h][new_n][new_m] < 0 and tomatoes[new_h][new_n][new_m] == 0:
                queue.append((new_h, new_n, new_m))
                new_visited = visited[cur[0]][cur[1]][cur[2]] + 1
                visited[new_h][new_n][new_m] = new_visited
                if new_visited > visited_max:
                    visited_max = new_visited

for height in range(h):
    for i in range(n):
        for j in range(m):
            if visited[height][i][j] < 0 and tomatoes[height][i][j] == 0:
                print(-1)
                sys.exit()

print(visited_max)
