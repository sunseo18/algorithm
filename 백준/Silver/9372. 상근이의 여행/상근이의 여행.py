import sys
from collections import deque

input = sys.stdin.readline


T = int(input())


for _ in range(T):
    _map = dict()
    answer = 0

    N, M = map(int, input().split())
    visited = [False]  * (N+1)
    for __ in range(M):

        a, b = map(int, input().split())

        if a in _map:
            _map[a].append(b)
        else:
            _map[a] = [b]
        if b in _map:
            _map[b].append(a)
        else:
            _map[b] = [a]

        start = a
    
    queue = deque([start])
    visited[start] = True
    while queue:
        cur = queue.popleft()

        for _next in _map[cur]:
            if not visited[_next]:
                visited[_next] = True
                answer += 1
                queue.append(_next)
                
    print(answer)

