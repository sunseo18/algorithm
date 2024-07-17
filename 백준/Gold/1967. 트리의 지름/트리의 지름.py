import sys
from collections import defaultdict

sys.setrecursionlimit(10**9)

input = sys.stdin.readline

n = int(input())

tree = defaultdict(list)

for _ in range(n-1):
    s, e, d = map(int, input().split())

    tree[s].append((e,d))
    tree[e].append((s, d))

        
visited = [False] * (n+1)

biggest_node = 0
longest_distance = 0

def dfs(node, distance):
    global biggest_node
    global longest_distance

    leaf_flag = True
    
    for child_node in tree[node]:
        child, next_distance = child_node
        if not visited[child]:
            leaf_flag = False
            visited[child] = True
            dfs(child, distance + next_distance)
            visited[child] = False

    if leaf_flag:
        if distance > longest_distance:
            biggest_node = node
            longest_distance = distance

visited[1] = True
dfs(1, 0)

longest_distance = 0
visited = [False] * (n+1)
visited[biggest_node] = True
dfs(biggest_node, 0)
print(longest_distance)
