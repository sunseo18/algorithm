def solution(maps):
    answer = []
    height = len(maps)
    width = len(maps[0])
    
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    visited = [[False for _ in range(width)] for _ in range(height)]
    
    for i in range(height):
        for j in range(width):
            if maps[i][j] == "X":
                visited[i][j] = True
            else:
                if visited[i][j] == True:
                    continue
                days = 0
                queue = [(i, j)]
                while queue:
                    cur_i, cur_j = queue.pop(0)
                    if visited[cur_i][cur_j] == True:
                        continue
                        
                    days += int(maps[cur_i][cur_j])
                    visited[cur_i][cur_j] = True
                    
                    for k in range(4):
                        next_i, next_j = cur_i+dx[k], cur_j+dy[k]
                        if next_i < 0 or next_j < 0 or next_i >= height or next_j >= width:
                            continue
                        else:
                            print(next_i, next_j)
                            if not visited[next_i][next_j] and maps[next_i][next_j] != "X":
                                queue.append((next_i, next_j))

                answer.append(days)
        
    if not answer:
        return [-1]
    return sorted(answer)