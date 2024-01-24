def solution(n):
    answer = 0
    
    answer_list = [0] * 60001
    
    answer_list[1] = 1
    answer_list[2] = 2
    for i in range(3, n+1):
        answer_list[i] = (answer_list[i-1] + answer_list[i-2]) % 1000000007
        
    return answer_list[n]