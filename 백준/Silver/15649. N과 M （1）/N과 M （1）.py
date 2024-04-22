import sys
from collections import defaultdict

dic = defaultdict(bool)

n, m = map(int, input().split())

arr = [0] * m

def dfs(arr, depth, dic):
    
    if depth == m:
        sys.stdout.write(" ".join(arr))
        sys.stdout.write("\n")
        return

    for i in range(1, n+1):
        
        if dic[i]:
            continue
        
        arr[depth] = str(i)
        dic[i] = True
        dfs(arr, depth +1, dic)
        dic[i] = False
            

dfs(arr, 0, dic)
