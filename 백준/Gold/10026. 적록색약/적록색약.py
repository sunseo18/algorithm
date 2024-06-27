import sys
sys.setrecursionlimit(10 ** 6)
n = int(sys.stdin.readline().strip())

array = []
for _ in range(n):
    array.append(sys.stdin.readline().strip())

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

def dfs_no(i, j, s):
    for d in range(4):
        ni, nj = i + di[d], j + dj[d]

        if 0 <= ni < n and 0 <= nj < n and not visited_no[ni][nj] and array[ni][nj] == s:
            visited_no[ni][nj] = True
            dfs_no(ni, nj, s)

def dfs_yes(i, j, s):
    for d in range(4):
        ni, nj =i + di[d], j + dj[d]

        if 0 <= ni < n and 0 <= nj < n and not visited_yes[ni][nj]:
            if s == 'R' or s == 'G':
                if array[ni][nj] == 'B':
                    continue
                else:
                    visited_yes[ni][nj] = True
                    dfs_yes(ni, nj, array[ni][nj])
            else:
                if array[ni][nj] == s:
                    visited_yes[ni][nj] = True
                    dfs_yes(ni, nj, s)
                    
answer_no = 0
visited_no = [[False for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited_no[i][j]:
            visited_no[i][j] = True
            dfs_no(i, j, array[i][j])
            answer_no += 1

answer_yes = 0
visited_yes = [[False for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited_yes[i][j]:
            visited_yes[i][j] = True
            dfs_yes(i, j, array[i][j])
            answer_yes += 1
    

sys.stdout.write(str(answer_no) + ' '+ str(answer_yes))

