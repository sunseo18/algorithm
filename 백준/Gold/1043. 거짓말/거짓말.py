import sys
from collections import deque

n, m = map(int, sys.stdin.readline().strip().split())


people = [-1 for _ in range(n+1)]
    
truth = list(map(int, sys.stdin.readline().strip().split()))
truth_length = truth[0]
if truth_length == 0:
    print(m)
    sys.exit()

parties = []
graph = dict()
for _ in range(m):
    party = list(map(int, sys.stdin.readline().strip().split()))
    parties.append(party[1:])
    
    for i in range(1, party[0]+1):
        if party[i] not in graph:
            graph[party[i]] = set(party[1:party[0]+1])
        else:
            graph[party[i]] = graph[party[i]] | set(party[1:party[0]+1])

for t in truth[1:]:
    queue = deque([t])
    people[t] = True
    
    while queue:
        cur = queue.popleft()

        if cur in graph:
            for vertex in graph[cur]:
                if people[vertex] == -1 :
                    people[vertex] = True
                    queue.append(vertex)

answer = 0
for party in parties:
    flag = False
    for p in party:
        if people[p] == True:
            flag = True
            break
    if not flag:
        answer += 1

print(answer)

