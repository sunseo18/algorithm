import sys

n = 5

move_x = [-1, 0, 1, 0]
move_y = [0, -1, 0, 1]

def bfs(board, distance, startX, startY):
    queue = [(startX, startY)]
    while queue:
        curX, curY = queue.pop(0)
        if board[curX][curY] == 1:
            return distance[curX][curY]
        for i in range(4):
            nextX, nextY = curX + move_x[i], curY + move_y[i]
            if ( nextX >= 0 and nextX < n ) and ( nextY >= 0 and nextY < n):
                if board[nextX][nextY] != -1 and distance[nextX][nextY] < 0:
                    queue.append((nextX, nextY))
                    distance[nextX][nextY] = distance[curX][curY] + 1
    return -1
        
        
board = []
for i in range(n):
    board.append(list(map(int, sys.stdin.readline().strip().split())))

startX, startY = map(int, sys.stdin.readline().strip().split())

distance = [[-1 for _ in range(n)] for _ in range(n)]

distance[startX][startY] = 0

print( bfs(board, distance, startX, startY))

