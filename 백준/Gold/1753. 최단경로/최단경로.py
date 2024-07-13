import sys
import heapq

INF = 1000000000

v, e = map(int, sys.stdin.readline().strip().split())

start = int(sys.stdin.readline().strip())

map_ = dict()
for _ in range(e):
    s, e, d = map(int, sys.stdin.readline().strip().split())


    if s in map_:
        map_[s].append((e, d))
    else:
        map_[s] = [(e, d)]


def dijkstra(start):
    d = [INF] * (v+1)

    q = [(0, start)]
    heapq.heapify(q)
    
    d[start] = 0

    while q:
        curd, curv = heapq.heappop(q)

        if d[curv] < curd:
            continue

        if curv not in map_:
            continue
        
        for nextv, nextd in map_[curv]:
            if curd + nextd < d[nextv]:
                d[nextv] = curd+nextd
                heapq.heappush(q, (curd+nextd, nextv))
    return d

result = dijkstra(start)
for i in range(1, v+1):
    if result[i] == INF:
        sys.stdout.write('INF')
    else:
        sys.stdout.write(str(result[i]))
    sys.stdout.write('\n')
