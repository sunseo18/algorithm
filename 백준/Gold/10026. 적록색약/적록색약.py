import sys
from collections import deque

n = int(sys.stdin.readline().strip())

array = []
for _ in range(n):
    array.append(sys.stdin.readline().strip())

visited_no = [[False for _ in range(n)] for _ in range(n)]
visited_yes = [[False for _ in range(n)] for _ in range(n)]

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

def bfs(i, j, s):
    queue = deque([(i, j, s)])

    while queue:
        ci, cj, s = queue.popleft()

        for d in range(4):
            ni, nj = ci+di[d], cj+dj[d]

            if 0 <= ni < n and 0 <= nj < n and not visited_no[ni][nj] and array[ni][nj] == s:
                visited_no[ni][nj] = True
                queue.append((ni, nj, s))

def bfs_yes(i, j, s):
    queue = deque([(i, j, s)])

    while queue:
        ci, cj, s = queue.popleft()


        for d in range(4):
            ni, nj = ci+di[d], cj+dj[d]

            if 0 <= ni <n and 0 <= nj < n and not visited_yes[ni][nj]:
                if array[i][j] == 'R' or array[i][j] == 'G':
                    if array[ni][nj] == 'B':
                        continue
                    else:
                        visited_yes[ni][nj] = True
                        queue.append((ni, nj, array[ni][nj]))

                else:
                    if array[ni][nj] == s:
                        visited_yes[ni][nj] = True
                        queue.append((ni, nj, s))
    
                    
answer_no = 0
answer_yes = 0

for i in range(n):
    for j in range(n):
        if not visited_no[i][j]:
            visited_no[i][j] = True
            bfs(i, j, array[i][j])
            answer_no += 1
        if not visited_yes[i][j]:
            visited_yes[i][j] = True
            bfs_yes(i, j, array[i][j])
            answer_yes+=1

    

sys.stdout.write(str(answer_no) + ' '+ str(answer_yes))

