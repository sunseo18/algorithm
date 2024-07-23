import sys
import heapq

input = sys.stdin.readline

n, e = map(int, input().split())

map_ = [ [float('inf') for _ in range(n+1)] for _ in range(n+1) ]

for _ in range(e):
    start, end, distance = map(int, input().split())

    map_[start][end] = distance
    map_[end][start] = distance


for i in range(n+1):
    for j in range(n+1):
        if i == j:
            map_[i][j] = 0

def get_min_index(array, visited, length):
    min_val = float('inf')
    min_index = -1
    
    for i in range(length):
        if not visited[i] and array[i] < min_val:
            min_index = i
            min_val = array[i]

    return min_index


def dijkstra(start):
    distance = map_[start]
    visited = [False] * (n+1)
    visited[0] = True
    visited[start] = True

    min_index = get_min_index(distance, visited, n+1)
    while min_index != -1:
        visited[min_index] = True
        for i in range(n+1):
            if not visited[i] and distance[min_index] + map_[min_index][i] < distance[i]:
                distance[i] = distance[min_index] + map_[min_index][i]
        min_index = get_min_index(distance, visited, n+1)


    return distance
    

v1, v2 = map(int, input().split())

v1_to_all = dijkstra(v1)

v1_to_start = v1_to_all[1]
v1_to_N = v1_to_all[n]

v2_to_all = dijkstra(v2)

v2_to_start = v2_to_all[1]
v2_to_N = v2_to_all[n]

v1_to_v2 = v2_to_all[v1]

answer = min(v1_to_start + v2_to_N + v1_to_v2, v2_to_start + v1_to_N + v1_to_v2)
if answer == float('inf'):
    print(-1)
else:
    print(answer)
