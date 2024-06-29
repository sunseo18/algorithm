import sys
from collections import deque

n = int(sys.stdin.readline().strip())

array = []

for _ in range(n):
    array.append(list(map(int, sys.stdin.readline().strip().split())))

vertex_dict = dict()

for i in range(n):
    queue = deque()
    visited = [False for _ in range(n)]
    visited[i] = True

    queue.append(i)
    visited[i] = True

    while queue:
        cur = queue.popleft()

        for nextv in range(n):
            if array[cur][nextv] == 1:
                if nextv == i:
                    if not i in vertex_dict.keys():
                        vertex_dict[i] = [i]
                    else:
                        vertex_dict[i].append(i)
                elif not visited[nextv]:
                    visited[nextv] = True
                    if not i in vertex_dict.keys():
                        vertex_dict[i] = [nextv]
                    else:
                        vertex_dict[i].append(nextv)
                    queue.append(nextv)
                
for key in vertex_dict.keys():
    for value in vertex_dict[key]:
        array[key][value] = 1

for i in range(n):
    for j in range(n):
        sys.stdout.write(str(array[i][j]))
        sys.stdout.write(' ')
    sys.stdout.write('\n')

