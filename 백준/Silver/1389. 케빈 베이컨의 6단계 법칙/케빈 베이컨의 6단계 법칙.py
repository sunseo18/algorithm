import sys
from collections import deque

n, m = map(int, sys.stdin.readline().strip().split())

array = [ [] for _ in range(n+1) ]

for i in range(m):
    s, e = map(int, sys.stdin.readline().strip().split())

    array[s].append(e)
    array[e].append(s)

min = 9999999999
kevin = 1
for i in range(1, n+1):
    answer = 0
    visited = [False for _ in range(n+1)]
    visited[i] = True

    queue = deque()
    for e in array[i]:
        if not visited[e]:
            queue.append((i, e, 1))
        visited[e] = True

    while queue:
        cs, ce, depth = queue.popleft()
        answer += depth
        
        for e in array[ce]:
            if not visited[e]:
                visited[e] = True
                queue.append((ce, e, depth+1))

    if answer < min:
        min = answer
        kevin = i
        
print(kevin)
