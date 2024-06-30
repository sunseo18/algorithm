import sys
sys.setrecursionlimit(10**6)

n, m =  map(int, sys.stdin.readline().strip().split())

array = []
for _ in range(n):
    array.append(list(map(int, sys.stdin.readline().strip().split())))

visited = [[False for _ in range(m)] for _ in range(n)]

di = [0, 0, 1, -1]
dj = [-1, 1, 0, 0]

answer = 0

def dfs(i, j, tmp, depth):
    global answer

    if depth == 4:
        answer = max(tmp, answer)
        return
    
    for d in range(4):
        ni, nj = i + di[d], j + dj[d]

        if 0 <= ni < n and 0 <= nj < m and not visited[ni][nj]:
            visited[ni][nj] = True
            dfs(ni, nj, tmp + array[ni][nj], depth + 1)
            visited[ni][nj] = False
def fy(i, j):
    global answer
    count = 0
    tmp = []
    for d in range(4):
        ni, nj = i+di[d], j+dj[d]
        if  0<= ni<n and 0<=nj<m:
            tmp.append(array[ni][nj])        
            count += 1
        

    if count == 4:
        tmp.sort(reverse=True)
        tmp.pop()
        answer = max(sum(tmp) + array[i][j], answer)
    elif count == 3:
        answer = max(answer, sum(tmp)+array[i][j])

for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(i, j, array[i][j], 1)
        visited[i][j] = False
        fy(i, j)
print(answer)
