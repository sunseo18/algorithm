import sys
sys.setrecursionlimit(10**9)


input = sys.stdin.readline


n, m = map(int, input().split())

numbers = list(map(int, input().split()))

numbers_dict = dict()


numbers.sort()

numbers = list(map(str, numbers))

index_visited = [False] * n
visited = dict()

def dfs(depth, tmp):
    if depth == m:
        tmp_str = " ".join(tmp)
        if tmp_str in visited:
            return
        else:
            visited[tmp_str] = 0
            for t in tmp:
                sys.stdout.write(t)
                sys.stdout.write(' ')
            sys.stdout.write('\n')
        
            return

    for i in range(n):
        if not index_visited[i]:
            tmp[depth] = numbers[i]
            index_visited[i] = True
            dfs(depth+1, tmp)
            index_visited[i] = False
        
dfs(0, [0] * m)
            
