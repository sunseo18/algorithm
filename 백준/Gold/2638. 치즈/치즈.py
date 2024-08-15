import sys

sys.setrecursionlimit(10**5)

input = sys.stdin.readline

CHEESE = 1
n, m = map(int, input().split())

outside = 0
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

map_ = []

for _ in range(n):
    map_.append(list(map(int, input().split())))


def dfs(i, j, next_):
    global outside
    global CHEESE

    map_[i][j] = next_

    for d in range(4):
        ni, nj = i + di[d], j + dj[d]

        if 0 <= ni < n and 0 <= nj < m and map_[ni][nj] != next_ and map_[ni][nj] != CHEESE:
            dfs(ni, nj, next_)

def delete_cheese(outside, deletes):
    global CHEESE

    for i in range(n):
        for j in range(m):
            if map_[i][j] == CHEESE:
                outside_cnt = 0
                for d in range(4):
                    ti = i + di[d]
                    tj = j + dj[d]

                    if map_[ti][tj] == outside:
                        outside_cnt += 1

                if outside_cnt >= 2:
                    deletes.append((i, j))

total_count = 0
next_ = 2

while True:
    dfs(0, 0, next_)
    outside = next_
    
    deletes = []
    delete_cheese(outside, deletes)

    if deletes:
        total_count += 1
    else:
        print(total_count)
        break

    for d in deletes:
        map_[d[0]][d[1]] = outside

    next_ += 1

    

    
