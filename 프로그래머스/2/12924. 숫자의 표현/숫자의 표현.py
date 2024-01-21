def solution(n):
    
    answer = 0
    for i in range(1, n):
        sum = i
        for j in range(i+1, n):
            sum += j
            if sum == n:
                answer += 1
                break
            if sum > n:
                break
        
    return answer+1