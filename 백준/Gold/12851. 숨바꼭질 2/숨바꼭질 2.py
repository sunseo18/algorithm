import sys
from collections import deque

MAX = 1000001
n, k = map(int, sys.stdin.readline().strip().split())

if n == k:
    sys.stdout.write('0')
    sys.stdout.write('\n')
    sys.stdout.write('1')
    sys.exit()

    
queue = deque([n])

distance = [0] * MAX
distance[n] = 1

fastest = 0
count = 0

while queue:
    cur = queue.popleft()

    if fastest != 0:
        if distance[cur] > fastest:
            continue
    
    if cur == k:
        if fastest == 0:
           fastest = distance[cur]
           count += 1
        else:
            count += 1

    move = [1, -1, cur]
    for i in range(3):
        next = cur + move[i]
        if 0 <= next < MAX:
            if distance[next] == 0 or (distance[next] == distance[cur] + 1):
                queue.append(next)
                distance[next] = distance[cur] +1

print(fastest -1 )
print(count)
    
    



