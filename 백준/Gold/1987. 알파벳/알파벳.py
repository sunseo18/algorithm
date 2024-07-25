import sys
input = sys.stdin.readline

R, C = map(int, input().split())

map_ = []
for _ in range(R):
    map_.append(list(input().strip()))

visited = [False] * 26

def alpha_to_index(alpha):
    return ord(alpha) - 65


max_depth = 1

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(i, j, depth):
    global max_depth
    if depth > max_depth:
        max_depth = depth
    
    for d in range(4):
        ni, nj = i + dx[d], j + dy[d]

        if 0 <= ni < R and 0 <= nj < C:
            if not visited[alpha_to_index(map_[ni][nj])]:
                visited[alpha_to_index(map_[ni][nj])] = True
                dfs(ni, nj, depth+1)
                visited[alpha_to_index(map_[ni][nj])] = False
    
visited[alpha_to_index(map_[0][0])] = True                        
dfs(0, 0, 1)
print(max_depth)
