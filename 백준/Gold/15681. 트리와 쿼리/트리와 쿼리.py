import sys
sys.setrecursionlimit(10**9)
n, r, q = map(int, sys.stdin.readline().split())

maps = dict()

for i in range(n-1):
    u, v = map(int, sys.stdin.readline().split())

    if u in maps:
        maps[u].append(v)
    else:
        maps[u] = [v]

    if v in maps:
        maps[v].append(u)
    else:
        maps[v] = [u]

def dfs(u, visited):
    global sub_tree
    
    visited[u] = True

    sub_tree[u] = 1

    for v in maps[u]:
        if not visited[v]:
            visited[v] = True
            sub_tree[u] += dfs(v, visited)

    return sub_tree[u]

visited = [False for _ in range(n+1)]
sub_tree = [0 for _ in range(n+1)]

dfs(r, visited)


for _ in range(q):
    question = int(sys.stdin.readline())
    print(sub_tree[question])

