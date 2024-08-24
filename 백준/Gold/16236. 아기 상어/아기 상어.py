import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

sea = []
shark_size = 2
shark_i , shark_j = 0, 0
answer = 0

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
    
for _ in range(n):
    sea.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        if sea[i][j] == 9:
            shark_i, shark_j = i, j

            break


def find_little_fish():
    result = []
    
    for i in range(n):
        for j in range(n):
            if 0 < sea[i][j] < shark_size:
                result.append((i, j))

    return result

def fish_and_distance(shark_i, shark_j, edable_fish_list):
    global n
    global shark_size
    result = []
    
    while edable_fish_list:
        fish_i, fish_j = edable_fish_list.pop()

        visited = [[False for _ in range(n)] for _ in range(n)]
        queue = deque([(shark_i, shark_j, 0)])
        visited[shark_i][shark_j] = True

        while queue:
            ci, cj, cd = queue.popleft()
            
            if ci == fish_i and cj == fish_j:
                result.append((cd, ci, cj))

    
            for d in range(4):
                ni, nj = ci + di[d], cj + dj[d]
                if 0 <= ni < n and 0 <= nj < n and sea[ni][nj] <= shark_size and not visited[ni][nj]:
                    visited[ni][nj] = True
                    queue.append((ni, nj, cd + 1))
                
    return sorted(result, reverse = True)

eaten_no = 0
sea[shark_i][shark_j] = 0

while True:
    edable_list = find_little_fish()
    if not edable_list:
        print(answer)
        break

    edable_distance = fish_and_distance(shark_i, shark_j, edable_list)
    if not edable_distance:
        print(answer)
        break


    distance, fish_i, fish_j = edable_distance.pop()
    
    # 이동, 먹기
    answer += distance
    sea[fish_i][fish_j] = 0
    shark_i, shark_j = fish_i, fish_j

    eaten_no += 1
    if eaten_no == shark_size:
        shark_size += 1
        eaten_no = 0
        

