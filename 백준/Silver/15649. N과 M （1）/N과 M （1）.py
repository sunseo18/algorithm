import sys
from collections import defaultdict

n, m = map(int, input().split())

dic = defaultdict(bool)

numbers = [ i for i in range(1, n+1) ]
def dfs(tmp, depth, dic):
    if depth == len(tmp):
        for t in tmp:
            sys.stdout.write(str(t))
            sys.stdout.write(' ')
        sys.stdout.write("\n")
        return
    for n in numbers:
        if dic[n]:
            continue
        tmp[depth] = n
        dic[n] = True
        
        dfs(tmp, depth + 1, dic)
        tmp[depth] = 0
        dic[n] = False

dfs([0]*m, 0, dic)
