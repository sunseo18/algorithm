import sys
input = sys.stdin.readline
n = int(input().strip())
board = []
for i in range(n):
    board.append(list(map(int, input().strip().split())))
#0가로 1세로 2대각
result = 0
def dfs(x2,y2,d):
    global result
    if x2 == n-1 and y2 == n-1:
            result += 1
    if d == 0 or d == 2:
        ny2 = y2 + 1
        if ny2 < n and board[x2][ny2] == 0:
            dfs(x2, ny2, 0)

    if d == 1 or d ==2:
        nx2 = x2 + 1
        if nx2 < n and board[nx2][y2] == 0:
            dfs(nx2, y2, 1)
    nx2 =x2 + 1
    ny2 = y2 +1
    if nx2 < n and ny2 < n and board[nx2][ny2] == 0 and board[nx2][ny2 - 1] == 0 and board[nx2 - 1][ny2] == 0:
        dfs(nx2, ny2, 2)

if board[n-1][n-1] == 1:
    print(0)
else:
    dfs(0,1,0)
    print(result)