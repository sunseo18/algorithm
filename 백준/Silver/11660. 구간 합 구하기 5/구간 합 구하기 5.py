import sys

N, M = map(int, sys.stdin.readline().strip().split())

array = []
for i in range(N):
    array.append(list(map(int, sys.stdin.readline().strip().split())))


accSumArray = [[ 0 for _ in range(N)] for _ in range(N)]

accSumArray[0][0] = array[0][0]

for i in range(N):
    for j in range(N):
        if i == 0 and j == 0:
            accSumArray[i][j] = array[i][j]
        elif i == 0:
            accSumArray[i][j] = array[i][j] + accSumArray[i][j-1]
        elif j == 0:
            accSumArray[i][j] = array[i][j] + accSumArray[i-1][j]


        else:
            accSumArray[i][j] = accSumArray[i-1][j] + accSumArray[i][j-1] + array[i][j] - accSumArray[i-1][j-1]

for i in range(M):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().strip().split())
    x1 -= 1
    y1 -= 1
    x2 -= 1
    y2 -= 1

    if x1 == 0 and y1 == 0:
        sys.stdout.write(str(accSumArray[x2][y2]))
    elif x1 == 0:
        sys.stdout.write(str(accSumArray[x2][y2] - accSumArray[x2][y1-1]))
    elif y1 == 0:
        sys.stdout.write(str(accSumArray[x2][y2] - accSumArray[x1-1][y2]))
    else:
        sys.stdout.write(str(accSumArray[x2][y2] - accSumArray[x2][y1-1] - accSumArray[x1-1][y2] + accSumArray[x1-1][y1-1]))

    sys.stdout.write('\n')

        
    