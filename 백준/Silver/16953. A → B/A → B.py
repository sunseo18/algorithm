import sys
from collections import deque

input = sys.stdin.readline

a, b = map(int, input().split())

visited = dict()
visited[a] = True
queue = deque([(a, 1)])

flag = False
while queue:
    cur_number, cur_depth = queue.popleft()

    if cur_number == b:
        print(cur_depth)
        flag = True
        sys.exit()


    next_2 = int(f"{cur_number}1")
    if next_2 <= b:
        if next_2 not in visited:
            visited[next_2] = True
            queue.append((next_2, cur_depth + 1))

    next_1 = cur_number*2
    if next_1 <= b:
        if next_1 not in visited:
            visited[next_1] = True
            queue.append((next_1, cur_depth + 1))


if not flag:
    print(-1)
