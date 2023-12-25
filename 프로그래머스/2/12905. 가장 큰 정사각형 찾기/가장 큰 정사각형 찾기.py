def solution(board):
    answer = 0
    row = len(board)
    col = len(board[0])
    
    if row == 1 and col == 1:
        if board[0][0] == 1:
            answer = 1
            
    rectangular = board.copy()

    for i in range(1, row):
        for j in range(1, col):
            if rectangular[i][j] != 0:
                rectangular[i][j] = min(rectangular[i-1][j], rectangular[i][j-1], rectangular[i-1][j-1]) + 1
                answer = max(rectangular[i][j], answer)

    return answer**2