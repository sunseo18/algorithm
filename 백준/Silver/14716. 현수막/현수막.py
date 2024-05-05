import sys

sys.setrecursionlimit(10000000)
m, n = map(int, sys.stdin.readline().strip().split())

hyunsumak = []

for i in range(m):
    hyunsumak.append(list(sys.stdin.readline().strip().split()))

di = [1, -1, 0, 0, 1, 1, -1, -1]
dj = [0, 0, 1, -1, -1, 1, 1, -1]
d_length = len(di)

def dfs(i, j):  
    if (0 > i or i >= m) or (0 > j or j >= n):
        return
    if hyunsumak[i][j] == '0':
        return

    hyunsumak[i][j] = '0'
    
    for x in range(d_length):
        next_i = i + di[x]
        next_j = j + dj[x]

        dfs(next_i, next_j)


answer = 0
    
for i in range(m):
    for j in range(n):
        if hyunsumak[i][j] == '1':
            answer += 1
            dfs(i, j)
            
print(answer)
