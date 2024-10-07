import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())


edges = dict()
degrees = [0 for _ in range(N)]

for _ in range(M):
    first, second = map(int, input().split())

    if first in edges:
        edges[first].append(second)

    else:
        edges[first] = [second]

    degrees[second-1] += 1

queue = deque()

for k in edges.keys():
    if degrees[k-1] == 0:
        queue.append(k)

answer = []
visited = [False] * N

while queue:
    start = queue.popleft()

    answer.append(start)
    visited[start-1] = True
    
    if start not in edges:
        continue
    
    for second in edges[start]:
        degrees[second-1] -= 1

        if degrees[second-1] == 0:
            queue.append(second)

for a in answer:
    sys.stdout.write(str(a))
    sys.stdout.write(' ')
            
for i in range(N):
    if not visited[i]:
        sys.stdout.write(str(i+1))
        sys.stdout.write(' ')
