import sys
sys.setrecursionlimit(10**6)
n, m = map(int, sys.stdin.readline().strip().split())

array = list(map(int, sys.stdin.readline().strip().split()))

array.sort()
visited = [False] * n

tmp = [0] * m

def dfs(i, depth):
    if depth == m:
        for t in tmp:
            sys.stdout.write(str(t))
            sys.stdout.write(' ')
        sys.stdout.write('\n')
        return

        
    for j in range(n):
        if not visited[j]:
            tmp[i] = array[j]
            visited[j] = True
            dfs(i+1, depth+1)
            visited[j] = False
            

dfs(0, 0)
