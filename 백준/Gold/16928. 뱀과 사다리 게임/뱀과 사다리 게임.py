from collections import deque
import sys

n, m = map(int, sys.stdin.readline().split())

visited = [False] * 101

ladder = dict()
snake = dict()

for _ in range(n):
    start, end = map(int, sys.stdin.readline().strip().split())
    ladder[start]= end
for _ in range(m):
    start, end = map(int, sys.stdin.readline().strip().split())
    snake[start] = end


queue = deque([(1, 0)])

while queue:
    cur, depth = queue.popleft()
    
    if cur == 100:
        print(depth)
        sys.exit()

    for i in range(1, 7):
        next = cur + i

        if 0 <= next <= 100 and not visited[next]:

            if next in ladder.keys():
                next = ladder[next]
            if next in snake.keys():
                next = snake[next]

            if not visited[next]:
                visited[next] = True
                queue.append((next, depth + 1))



