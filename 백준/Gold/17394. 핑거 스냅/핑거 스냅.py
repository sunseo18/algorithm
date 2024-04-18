import sys
from collections import defaultdict

B_MAX = 100000
sosu = [ 0 ] * 100001

for i in range(2, 100001):
    if sosu[i] == 1:
        continue
    for j in range(2, B_MAX // i + 1):
        sosu[i*j] = 1


t = int(sys.stdin.readline().strip())

for _ in range(t):
    n, a, b = map(int, sys.stdin.readline().strip().split())

    if 0 not in sosu[a:b+1]:
        print(-1)
        continue
    
    flag = 0
    visited = defaultdict(int)
    queue = [n]

    visited[n] = 1
    
    while queue:
        cur = queue.pop(0)
        if a <= cur and cur <= b:
            if sosu[cur] == 0:
                flag = 1
                sys.stdout.write(str(visited[cur]-1))
                break
        tmp = cur // 3
        if visited[tmp] == 0:
            queue.append(tmp)
            visited[tmp] = visited[cur] + 1
        tmp = cur // 2
        if visited[tmp] == 0:
            queue.append(tmp)
            visited[tmp] = visited[cur] + 1
        tmp = cur + 1
        if visited[tmp] == 0:
            queue.append(tmp)
            visited[tmp] = visited[cur] + 1
        tmp = cur - 1
        if visited[tmp] == 0:
            queue.append(tmp)
            visited[tmp] = visited[cur] + 1

    if flag == 0:
        sys.stdout.write('-1')
    sys.stdout.write('\n')
