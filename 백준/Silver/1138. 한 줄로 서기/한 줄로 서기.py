import sys

n = int(sys.stdin.readline())

numbers = list(sys.stdin.readline().split())

people = [i for i in range(1, n+1)]
visited = [False for _ in range(n)]

def dfs(tmp, i):
    if i == n:
        if ''.join(numbers) == checkBigger(tmp):
            for t in tmp:
                sys.stdout.write(str(t))
                sys.stdout.write(' ')
        return

    for x in range(n):
        if not visited[x]:
            tmp[i] = people[x]
            visited[x] = True
            dfs(tmp, i+1)
            visited[x] = False
    
def checkBigger(array):
    result = [0 for _ in range(n)]
    for i in range(n):
        tmp = 0
        for j in range(0, i):
            if array[j] > array[i]:
                tmp += 1
        result[array[i]-1] = str(tmp)

    return ''.join(result)


dfs([0 for _ in range(n)], 0)
