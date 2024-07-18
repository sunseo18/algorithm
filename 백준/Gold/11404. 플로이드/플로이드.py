import sys
INF = float('inf')
input = sys.stdin.readline

n = int(input())
m = int(input())

map_ = [[INF for _ in range(n)]  for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i == j:
            map_[i][j] = 0
            
for _ in range(m):
    a, b, c = map(int, input().split())

    map_[a-1][b-1] = min(map_[a-1][b-1], c)

for k in range(n):
    for i in range(n):
        for j in range(n):
            map_[i][j] = min(map_[i][k] + map_[k][j], map_[i][j])       

for i in range(n):
    for j in range(n):
        if map_[i][j] == INF:
            sys.stdout.write('0')
            sys.stdout.write(' ')
            continue
        sys.stdout.write(str(map_[i][j]))
        sys.stdout.write(' ')
    sys.stdout.write('\n')
