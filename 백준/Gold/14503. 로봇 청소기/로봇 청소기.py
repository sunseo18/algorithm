import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int, input().split())

si, sj, d = map(int, input().split())

_map = []

for i in range(N):
    _map.append(list(map(int, input().split())))


di= [0, 0, 1, -1]
dj= [1, -1, 0, 0]

def reverse(i, j, direction):
    if direction == 1:
        return (i, j-1)
    elif direction == 2:
        return (i-1, j)
    elif direction == 3:
        return (i, j+1)
    else:
        return (i+1, j)
    
def rotate(direction):
    if direction == 1:
        return 0
    elif direction == 2:
        return 1
    elif direction == 3:
        return 2
    else:
        return 3

def move(i, j, direction):
    if direction == 1:
        return (i, j+1)
    elif direction == 2:
        return (i+1, j)
    elif direction == 3:
        return (i, j-1)
    else:
        return (i-1, j)
    
answer = 0


def dfs(i, j, direction):
    global answer
    
    if _map[i][j] == 0:
        answer += 1
    _map[i][j] = 2


    # 현재 칸 주변 청소되지 않은 빈 칸이 있는지 검사
    all_clean_flag = True
    for k in range(4):
        ni, nj = i + di[k], j + dj[k]
        if 0 <= ni < N and 0 <= nj < M:
            if _map[ni][nj] == 0:
                all_clean_flag = False
    
    # 네 방향 다 청소 됨
    if all_clean_flag:
        ri, rj = reverse(i, j, direction)
        if (ri < 0 or ri >= N) or (rj < 0 or rj >= M):
            return
        if _map[ri][rj] == 1:
            return
        else:
            dfs(ri, rj, direction)

    # 네 방향 중 청소 안 된 곳 있음
    else:
        nd = rotate(direction)
        ni, nj = move(i, j, nd)

        if 0 <= ni < N and 0 <= nj < M and _map[ni][nj] != 1 and _map[ni][nj] == 0:
            dfs(ni, nj, nd)
            return
                        
        dfs(i, j, nd)
              
dfs(si, sj, d)
print(answer)        
