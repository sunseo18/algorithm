import sys
from collections import deque
from collections import defaultdict

n, k = map(int, sys.stdin.readline().strip().split())

queue = deque([(n, 0)])
visited = defaultdict(bool)

while queue:
    cur, depth = queue.popleft()

    if cur == k:
        print(depth)
        sys.exit()
        
    next = cur+1
    if not visited[next] and 100000 >= next >= 0:
        visited[next]= True
        queue.append((next, depth+1))

    next = cur-1
    if not visited[next] and 100000 >= next >= 0:
        visited[next]= True
        queue.append((next, depth+1))

    next = cur*2
    if not visited[next] and 100000 >= next >= 0:
        visited[next] = True
        queue.append((next, depth+1))


