import sys

sys.setrecursionlimit(1000000000)
n, m = map(int, sys.stdin.readline().strip().split())

maps=[]
for i in range(n):
    maps.append(list(sys.stdin.readline().strip()))

def dfs(i, j):
    global v_no
    global k_no

    if i < 0 or i >= n or j < 0 or j >= m:
        return

    if maps[i][j] == '#':
        return

    if maps[i][j] == 'v':
        v_no += 1
        maps[i][j] = '#'

    elif maps[i][j] == 'k':
        k_no += 1
        maps[i][j] = '#'

    elif maps[i][j] == '.':
        maps[i][j] = '#'

    dfs(i+1, j)
    dfs(i, j+1)
    dfs(i-1, j)
    dfs(i, j-1)
    
v_answer, k_answer = 0, 0

for i in range(n):
    for j in range(m):
        if maps[i][j] == 'v' or maps[i][j] == 'k':
            v_no, k_no = 0, 0
            dfs(i, j)

            if k_no > v_no:
                k_answer += k_no
            else:
                v_answer += v_no

print(k_answer, v_answer)
