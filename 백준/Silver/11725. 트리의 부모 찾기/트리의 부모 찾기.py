import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n = int(input())

tree = dict()

for _ in range(n-1):
    v1, v2 = map(int, input().split())

    if v1 in tree:
        tree[v1].append(v2)
    else:
        tree[v1] = [v2]

    if v2 in tree:
        tree[v2].append(v1)
    else:
        tree[v2] = [v1]
        
parent_array = [0] * 100001

visited = [False] * 100001

def dfs(cur):
    for nv in tree[cur]:
        if not visited[nv]:
            visited[nv] = True
            parent_array[nv] = cur
            dfs(nv)
            
visited[1] = True
dfs(1)

for i in range(2, 100001):
    if parent_array[i] == 0:
        break
    else:
        sys.stdout.write(str(parent_array[i]))
        sys.stdout.write('\n')
