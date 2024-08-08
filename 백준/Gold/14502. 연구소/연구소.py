import sys
import copy 
input = sys.stdin.readline

n, m = map(int, input().split())

map_ = []
for _ in range(n):
    map_.append(list(map(int, input().split())))

visited = [[False for _ in range(m)] for _ in range(n)]

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

start_i, start_j = 0, 0
flag = False
for i in range(n):
    for j in range(m):
        if map_[i][j] == 0:
            start_i = i
            start_j = j
            flag = True
            break
    if flag:
        break


def spread_virus(virus_test, i, j):
    for d in range(4):
        ni = i + di[d]
        nj = j + dj[d]

        if 0 <= ni < n and 0 <= nj < m and virus_test[ni][nj] == 0:
            virus_test[ni][nj] = 2
            spread_virus(virus_test, ni, nj)

answer = 0    
def dfs(i, j, count_1):
    global answer
    if count_1 == 3:
        
        virus_test = copy.deepcopy(map_)
        for ti in range(n):
            for tj in range(m):
                if virus_test[ti][tj] == 2:
                    spread_virus(virus_test, ti, tj)
            
        tmp = 0
        for ti in range(n):
            for tj in range(m):
                if virus_test[ti][tj] == 0:
                    tmp += 1
        
        answer = max(answer, tmp)
        return

    for ni in range(0, n):
        for nj in range(0, m):
            if not visited[ni][nj] and map_[ni][nj] == 0:
                visited[ni][nj] = True
                map_[ni][nj] = 1
                dfs(ni, nj, count_1 + 1)
                visited[ni][nj] = False
                map_[ni][nj] = 0
                
    
dfs(0, 0, 0)
print(answer)
