import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

k2 = n//3


height = n
width = n*2 - 1
result = [ [' ' for _ in range(width)] for _ in range(height)]

def dfs(n, i, j):
    if n == 3:
        result[i][j] = '*'
        result[i+1][j-1] = '*'
        result[i+1][j+1] = '*'
        for x in range(j-2, j+3):
            result[i+2][x] = '*'
        return

    dfs(n//2, i, j)
    dfs(n//2, i + n//2, j-(n//2))
    dfs(n//2, i + n//2, j+(n//2))

    
        
dfs(n, 0, (width)//2)

for i in range(height):
    for j in range(width):
        sys.stdout.write(result[i][j])

    sys.stdout.write('\n')

