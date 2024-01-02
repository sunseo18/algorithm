def move_right(board, i, j):
    while True:
        new_j = j+1
        if new_j < len(board[0]) and board[i][new_j] != 'D':
            j = new_j
        else:
            break
    return(i, j)

def move_left(board, i, j):
    while True:
        new_j = j-1
        if new_j >= 0 and board[i][new_j] != 'D':
            j = new_j
        else:
            break
    return(i, j)

def move_up(board, i, j):
    while True:
        new_i = i-1
        if new_i >= 0 and board[new_i][j] != 'D':
            i = new_i
        else:
            break
    return(i, j)

def move_down(board, i, j):
    while True:
        new_i = i+1
        if new_i < len(board) and board[new_i][j] != 'D':
            i = new_i
        else:
            break
    return(i, j)
    
def solution(board):
    
    row = len(board)
    col = len(board[0])
    
    visited = [[False] * col for _ in range(row)]
    
    for i in range(row):
        for j in range(col):
            if board[i][j] == 'R':
                R_i, R_j = i, j
            elif board[i][j] == 'G':
                G_i, G_j = i, j
    
    count = -1
    queue = [(R_i, R_j, 0)]
    while queue:
        cur = queue.pop(0)
        visited[cur[0]][cur[1]] = True
        count += 1
        if cur[0] == G_i and cur[1] == G_j:
            return cur[2]
        
        moved_right = move_right(board, cur[0], cur[1])
        moved_left = move_left(board, cur[0], cur[1])
        moved_down = move_down(board, cur[0], cur[1])
        moved_up = move_up(board, cur[0], cur[1])
        if moved_right[1] != cur[1] and not visited[moved_right[0]][moved_right[1]]:
            queue.append((moved_right[0], moved_right[1], cur[2]+1))
        if moved_left[1] != cur[1] and not visited[moved_left[0]][moved_left[1]]:
            queue.append((moved_left[0], moved_left[1], cur[2]+1))
        if moved_down[0] != cur[0] and not visited[moved_down[0]][moved_down[1]]:
            queue.append((moved_down[0], moved_down[1], cur[2]+1))
        if moved_up[0] != cur[0] and not visited[moved_up[0]][moved_up[1]]:
            queue.append((moved_up[0], moved_up[1], cur[2]+1))
        
    return -1
    