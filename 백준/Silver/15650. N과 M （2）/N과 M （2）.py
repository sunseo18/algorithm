import sys

n, m = map(int, input().split())

arr = [0] * m

def dfs(arr, depth):
    
    if depth == m:
        sys.stdout.write(" ".join(arr))
        sys.stdout.write("\n")
        return

    for i in range(1, n+1):
        if depth != 0 and str(i) <= arr[depth-1]:
            continue
        
        arr[depth] = str(i)
        dfs(arr, depth +1)
            

dfs(arr, 0)
