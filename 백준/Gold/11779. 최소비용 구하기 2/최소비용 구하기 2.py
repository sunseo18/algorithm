import sys
import heapq

input = sys.stdin.readline

n = int(input())
m = int(input())


map_ = dict()

dijkstra = [float('inf') for _ in range(n+1)]
prev_node = [0 for _ in range(n+1)]

for _ in range(m):
    a, b, d = map(int, input().split())
    
    if a in map_:
        map_[a].append((d, b))
    else:
        map_[a] = [(d, b)]
        

start, end = map(int, input().split())

heap = []
heapq.heapify(heap)
heapq.heappush(heap, (0, start))

dijkstra[start] = 0

while heap:
    cur_d, cur_b = heapq.heappop(heap)

    if cur_d > dijkstra[cur_b]:
        continue

    if cur_b not in map_:
        continue
    
    for next_d, next_node in map_[cur_b]:
        cost = cur_d + next_d
        
        if dijkstra[next_node] > cost:
            dijkstra[next_node] = cost
            prev_node[next_node] = cur_b
            heapq.heappush(heap, (cost, next_node))


path = [end]
now = end
while now != start:
    now = prev_node[now]
    path.append(now)

path.reverse()

print(dijkstra[end])
print(len(path))
print(' '.join(map(str, path)))
    
