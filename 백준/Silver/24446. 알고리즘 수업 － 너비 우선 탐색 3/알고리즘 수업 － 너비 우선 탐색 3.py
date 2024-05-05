import sys
from collections import deque

n, m, r = map(int, sys.stdin.readline().strip().split())

vertex = [ [] for _ in range(n+1)]
visited = [ -1 for _ in range(n+1)]
visited[r] = 0

for i in range(m):
    u, v = map(int, sys.stdin.readline().strip().split())

    vertex[u].append(v)
    vertex[v].append(u)


queue = deque([r])

while queue:
    cur = queue.popleft()

    for v in vertex[cur]:
        if visited[v] == -1:
            visited[v] = visited[cur] + 1
            queue.append(v)

for i in range(1, n+1):
    print(visited[i])
    

    
