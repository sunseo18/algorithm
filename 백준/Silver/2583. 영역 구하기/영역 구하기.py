import sys

sys.setrecursionlimit(10**7)

m, n, k = map(int, sys.stdin.readline().strip().split())

array = [[0 for _ in range(m)] for _ in range(n)]


for i in range(k):
    leftX, leftY, rightX, rightY = map(int, sys.stdin.readline().strip().split())

    for x in range(leftX, rightX):
        for y in range(leftY, rightY):
            array[x][y] = 1

def dfs(i, j):
    global result
    if not ((n > i >= 0) and (m > j >= 0)):
        return
    
    if array[i][j] != 0:
        return
    
    else:
        array[i][j] = 1
        result += 1

        dfs(i-1, j)
        dfs(i+1, j)
        dfs(i, j-1)
        dfs(i, j+1)

answersLength = 0
answers = []
for i in range(n):
    for j in range(m):
        if array[i][j] != 1:
            result = 0
            dfs(i, j)
            if result != 0:
                answersLength += 1
                answers.append(result)

print(answersLength)
for a in sorted(answers):
    print(a, end= " ")
    
