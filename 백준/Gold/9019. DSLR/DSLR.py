import sys
from collections import deque

t = int(sys.stdin.readline().strip())

for _ in range(t):

    a, b = map(int, sys.stdin.readline().strip().split())


    queue = deque([(a, '')])
    visited = [False] * 100000
    visited[a] = True

    while queue:
        cur, cmd = queue.popleft()

        if cur == b:
            sys.stdout.write(cmd)
            sys.stdout.write('\n')
            break

        next_1 = cur * 2 % 10000

        if not visited[next_1]:
            visited[next_1] = True
            queue.append((next_1, cmd + 'D'))

        if cur == 0:
            next_2 = 9999
        else:
            next_2 = cur - 1

        if not visited[next_2]:
            visited[next_2] = True
            queue.append((next_2, cmd + 'S'))


        top = cur//1000
        left = cur % 1000
        next_3 =  left*10 + top
        if not visited[next_3]:
            visited[next_3] = True
            queue.append((next_3, cmd + 'L'))

        top_3 = cur//10
        last = cur%10
        next_4 = last * 1000 + top_3
        if not visited[next_4]:
            visited[next_4] = True
            queue.append((next_4, cmd + 'R'))
                            
