import sys
from collections import deque
from collections import defaultdict

a, b = map(int, sys.stdin.readline().strip().split())

queue = deque()
visited = defaultdict(int)

queue.appendleft(a)
visited[a] = 1

while queue:
    cur = queue.popleft()
    if cur == b:
        print(visited[cur] - 1)
        sys.exit()
    cur_depth = visited[cur]
    
    next_1 = cur + 1
    if next_1 <= b:
        if visited[next_1] == 0:
            queue.append(next_1)
            visited[next_1] = cur_depth + 1
        
    next_2 = cur * 2
    if next_2 <= b:
        if visited[next_2] == 0:
            queue.append(next_2)
            visited[next_2] = cur_depth + 1




    
