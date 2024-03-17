M, N = map(int, input().split())

chess_board = []
for _ in range(M):
    chess_board.append(input())


answer = N*M
# chess_board의 [i,j]번째를 왼쪽 꼭짓점으로하는 체스 판의 변경해야하는 블럭 수 구하기
def calc(chess_board, I, J):
    w_start = 0
    b_start = 0

    for i in range(I, I+8):
        for j in range(J, J+8):
            if i % 2 == 0:
                if j % 2 == 0:
                    if chess_board[i][j] == 'W':
                        b_start += 1
                    else:
                        w_start += 1
                else:
                    if chess_board[i][j] == 'B':
                        b_start += 1
                    else:
                        w_start += 1
            else:
                if j % 2 == 0:
                    if chess_board[i][j] == 'B':
                        b_start += 1
                    else:
                        w_start += 1
                else:
                    if chess_board[i][j] == 'W':
                        b_start += 1
                    else:
                        w_start += 1
    return min(b_start, w_start)
            
    
    
for i in range(0, M - 7):
    for j in range(0, N - 7):
        tmp = calc(chess_board, i, j)
        if tmp < answer:
            answer = tmp

print(answer)
