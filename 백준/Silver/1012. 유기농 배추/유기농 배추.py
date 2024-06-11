import sys

t = int(sys.stdin.readline().strip())

sys.setrecursionlimit(9999999)
answer = 0
di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

def dfs(i, j, maps, m, n):

    maps[i][j] = 0
    
    for d in range(4):
        ni, nj = i + di[d], j + dj[d]

        if 0 <= ni < n and 0 <= nj < m and maps[ni][nj] != 0:
            dfs(ni, nj, maps, m, n)
            
    
for _ in range(t):
    m, n, k = map(int, sys.stdin.readline().strip().split())

    maps = [[0 for _ in range(m)] for _ in range(n)]

    for _ in range(k):
        j, i = map(int, sys.stdin.readline().strip().split())

        maps[i][j] = 1

    answer = 0
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 1:
                answer += 1
                dfs(i, j, maps, m, n)

    print(answer)
