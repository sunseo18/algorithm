import sys
import heapq

input = sys.stdin.readline

n = int(input())
m = int(input())

map_ = [ [] for _ in range(n+1) ]


for _ in range(m):
    start, end, distance = map(int, input().split())

    map_[start].append((end, distance))


def dijkstra(start, end):
    queue = []
    distance = [float('inf')] * (n+1)

    distance[start] = 0

    heapq.heappush(queue, (0, start))
    
    while queue:
        cd, cn = heapq.heappop(queue)

        if distance[cn] < cd:
            continue
        
        for next_node, next_distance in map_[cn]:
            if cd + next_distance < distance[next_node]:
                distance[next_node]  = cd + next_distance
                heapq.heappush(queue, (cd+next_distance, next_node))

    return distance[end]

start, end = map(int, input().split())

print(dijkstra(start, end))
