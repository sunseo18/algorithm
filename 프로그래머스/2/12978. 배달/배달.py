MAX = 500001

def get_smallest_node(d, visited):
    min = MAX
    min_idx = 0
    for i in range(2, len(d)):
        if not visited[i]:
            if d[i] < min:
                min = d[i]
                min_idx = i
    return min_idx
            
    
def solution(N, road, K):
    answer = 0
    
    w = [[MAX for _ in range(N+1)] for _ in range(N+1)]
    visited = [False, False] + ([False] * (N-1))
    for r in road:
        if r[2] < w[r[0]][r[1]]:
            w[r[0]][r[1]] = r[2]
            w[r[1]][r[0]] = r[2]
    
    for i in range(N+1):
        for j in range(N+1):
            if i == j:
                w[i][j] = 0
                
    d = w[1]

    visited[1] = True
    last = 1
    for _ in range(2, N+1):
        for i in range(2, N+1):
            if not visited[i]:
                d[i] = min(d[i], d[last] + w[last][i])
                
        last = get_smallest_node(d, visited)
        visited[last] = True

         
    for l in d:
        if l <= K:
            answer += 1
            
    return answer