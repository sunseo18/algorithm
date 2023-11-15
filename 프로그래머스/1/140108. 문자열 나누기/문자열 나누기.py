
    
def solution(s):
    answer = 0
    i = 1
    same = 1
    diff = 0
    
    while s:
        length = len(s)
        if length == 1:
            return 1
        
        x = s[0]
        if s[i] == x:
            same += 1
            
        elif s[i] != x:
            diff += 1
        
        if same == diff:
            answer += 1
            
            if i == length-3 or i == length-2:
                answer += 1
                break
            
            s = s[i+1:]
            same, diff, i = 1, 0, 1
            continue
            
        if i == length-2 or i == length-1:
            answer += 1
            break

        i += 1
        
    return answer