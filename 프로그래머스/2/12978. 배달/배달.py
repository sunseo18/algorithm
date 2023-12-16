MAX = 500001
def solution(N, road, K):
    answer = 0
    
    w = [[MAX for _ in range(N+1)] for _ in range(N+1)]
    for r in road:
        if r[2] < w[r[0]][r[1]]:
            w[r[0]][r[1]] = r[2]
            w[r[1]][r[0]] = r[2]
            
    for i in range(N + 1):
        w[i][i] = 0
        
    for path in range(N + 1):
        for i in range(N + 1):
            for j in range(N + 1):
                if w[i][j] > w[i][path] + w[path][j]:
	                    w[i][j] = w[i][path] + w[path][j]
        
    for l in w[1]:
        if l <= K:
            answer += 1
            
    return answer