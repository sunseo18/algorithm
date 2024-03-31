import sys
from collections import defaultdict

n, m = map(int, input().split())

numbers = [ i for i in range(1, n+1) ]
def dfs(tmp, depth):
    if depth == len(tmp):
        for t in tmp:
            sys.stdout.write(str(t))
            sys.stdout.write(' ')
        sys.stdout.write("\n")
        return
    for n in numbers:
        if depth != 0 and tmp[depth-1] > n:
            continue
        tmp[depth] = n
        
        dfs(tmp, depth + 1)
        tmp[depth] = 0
        
dfs([0]*m, 0)
