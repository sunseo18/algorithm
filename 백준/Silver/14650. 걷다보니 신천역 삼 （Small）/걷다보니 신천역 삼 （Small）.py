import sys
from collections import deque

n = int(sys.stdin.readline().strip())

if n == 1:
    print(0)
    sys.exit()

tmp = deque()

answer = 0
def dfs(tmp, depth, sum):
    global answer
    if depth == n:
        if sum % 3 == 0:
            answer += 1
        return
    
    tmp.append(0)
    dfs(tmp, depth + 1, sum)
    tmp.pop()
    
    tmp.append(1)
    dfs(tmp, depth + 1, sum + 1)
    tmp.pop()

    tmp.append(2)
    dfs(tmp, depth + 1, sum + 2)
    tmp.pop()

dfs([1], 1, 1)
dfs([2], 1, 2)


print(answer)
