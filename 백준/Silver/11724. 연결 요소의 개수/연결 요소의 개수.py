import sys
sys.setrecursionlimit(9999999)

n, m = map(int, sys.stdin.readline().strip().split())

maps = [[] for i in range(n)]
visited = [False for i in range(n)]

for i in range(m):
    u, v = map(int, sys.stdin.readline().strip().split())

    maps[u-1].append(v-1)
    maps[v-1].append(u-1)

def dfs(node):
    global visited
    visited[node] = True

    for v in maps[node]:
        if not visited[v]:
            dfs(v)
         
answer = 0
for i in range(n):
    if not visited[i]:
        answer += 1
        dfs(i)
            
    
print(answer)
