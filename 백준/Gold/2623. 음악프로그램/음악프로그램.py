import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())


member_in = [0 for i in range(n+1)]
vertex = { i: [] for i in range(1, n+1) }

for _ in range(m):
    members = list(map(int, sys.stdin.readline().split()))

    for i in range(2, len(members)):
        member_in[members[i]] += 1
        vertex[members[i-1]].append(members[i])
    

queue = deque()
for i in range(1, n+1):
    if member_in[i] == 0:
        queue.append(i)

answer = []
while queue:
    cur = queue.popleft()
    answer.append(cur)
    
    for node in vertex[cur]:
        member_in[node] -= 1
        if member_in[node] == 0:
            queue.append(node)

if len(answer) != n:
    print(0)
else:
    for a in answer:
        sys.stdout.write(str(a))
        sys.stdout.write('\n')
    
        
