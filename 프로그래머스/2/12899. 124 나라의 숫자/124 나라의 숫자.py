def solution(n):
    answer = ''
    
    hae = n
    while hae > 0:
        mod = hae % 3
        hae = hae // 3
        
        if mod == 0:
            answer = '4' + answer
            hae -= 1
        elif mod == 1:
            answer = '1' + answer
        elif mod == 2:
            answer = '2' + answer
            
    return answer