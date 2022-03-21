from collections import deque
n, m, start = map(int, input().split())
# inputString = input().split()
# n, m, start = map(int, inputString[:3].split())
# graphlist = inputString[3:]
# print(n, m, start)
# print(graphlist)

graph = [[] for _ in range(n+1)]
for _ in range(m):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)

for i in range(n+1):
    graph[i] = sorted(graph[i])

visited = [False] * (n+1)

def dfs(start, visited):
    global graph
    visited[start] = True
    print(start, end=" ")
    for v in graph[start]:
        if not visited[v]:
            dfs(v, visited)

def bfs(start, visited):
    global graph
    queue = deque([start])
    visited[start] = True
    while queue:
        visit = queue.popleft()
        print(visit, end=" ")
        for v in graph[visit]:
            if not visited[v]:
                queue.append(v) 
                visited[v] = True

dfs(start, visited)
visited = [False] * (n+1)
print()
bfs(start, visited)