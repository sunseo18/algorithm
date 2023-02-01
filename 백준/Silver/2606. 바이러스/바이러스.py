def dfs(src, v):
    if visited[src]:
        return
    
    visited[src] = True

    for dst in range(1, v+1):
        if computers[src][dst]:
            computers[src][dst] = 0
            computers[dst][src] = 0
            dfs(dst, v)
            
v = int(input()) # 전체 컴퓨터의 수 (노드 수)
e = int(input()) # 연결 수 (간선 수)
computers = [[0 for _ in range(v+1)] for _ in range(v+1)]
visited = [False for _ in range(v+1)]

for i in range(e):
    src, dst = list(map(int, input().split()))
    computers[src][dst] = 1
    computers[dst][src] = 1

dfs(1, v)

answer = 0
for isVisit in visited:
    if isVisit:
        answer += 1

print(answer - 1)