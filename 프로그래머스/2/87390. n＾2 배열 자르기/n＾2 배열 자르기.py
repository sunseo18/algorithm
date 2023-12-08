def solution(n, left, right):
    left_div = left // n
    right_div = right // n
    right_idx = right+1
    
    answer = []
    for div in range(left_div, right_div+1):
        answer += [div+1] * (div+1)
        for i in range(div+2, n+1):
            answer.append(i)         
    
    if (left_div) != 0:
        right_idx = right - (n*left_div) + 1
    
    print(right_idx)
    return answer[left % n: right_idx]