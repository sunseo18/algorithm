import sys
from collections import deque

n, k = map(int, sys.stdin.readline().strip().split())

direction_x = [0, 0, 1, -1]
direction_y = [1, -1, 0, 0]

maps = []
for _ in range(n):
    maps.append(list(map(int, sys.stdin.readline().strip().split())))

vacts = []

for i in range(n):
    for j in range(n):
        if maps[i][j] != 0:
            vacts.append((maps[i][j], i, j, 0))
            
s, x, y = map(int, sys.stdin.readline().strip().split())

vacts.sort()
vacts = deque(vacts)

for i in range(s):
    while vacts and vacts[0][-1] == i:
        vact_no, cur_x, cur_y, second = vacts.popleft()
           
        for d in range(4):
            next_x = cur_x + direction_x[d]
            next_y = cur_y + direction_y[d]
            if  0<=next_x<n and 0<=next_y<n and maps[next_x][next_y] == 0:
                maps[next_x][next_y] = vact_no
                vacts.append((vact_no, next_x, next_y, second + 1))
                    
print(maps[x-1][y-1])

