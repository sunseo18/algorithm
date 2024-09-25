import sys

N = 9

sudoku = []
for i in range(N):
    sudoku.append(list(map(int, list(sys.stdin.readline().rstrip()))))


def possible(i, j, v):
    # 세로
    for col in range(N):
        if col != i and sudoku[col][j] == v:
            return False

    # 가로
    for row in range(N):
        if row != j and sudoku[i][row] == v:
            return False

    # 사각형
    start_i = i//3 * 3
    start_j = j//3 * 3


    for col in range(start_i, start_i+3):
        for row in range(start_j, start_j+3):

            if (col != i and row != j) and sudoku[col][row] == v:
                return False

    return True

def count_zero(sudoku):
    count = 0
    for col in range(N):
        for row in range(N):
            if sudoku[col][row] == 0:
                count += 1

    return count

def dfs(i, j, depth, zero_no):
    #print(i, j, depth)
    if depth == zero_no:
        for i in range(N):
            for j in range(N):
                sys.stdout.write(str(sudoku[i][j]))
            sys.stdout.write('\n')
        sys.exit()

    if sudoku[i][j] == 0:
        for v in range(1, N+1):
            if possible(i, j, v):
                sudoku[i][j] = v
                if j == N-1:
                    dfs(i+1, 0, depth+1, zero_no)
                else:
                    dfs(i, j+1, depth+1, zero_no)
                sudoku[i][j] = 0
    else:
        if j == N-1:
            dfs(i+1, 0, depth, zero_no)
        else:
            dfs(i, j+1, depth, zero_no)


zero_no = count_zero(sudoku)

dfs(0, 0, 0, zero_no)
    
