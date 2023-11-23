def solution(s):
    
    stack = list()    
    
    for c in s:
        if not stack or c != stack[-1]:
            stack.append(c)
        else: 
            stack.pop()        
        
    answer = 1 if not stack else 0

    return answer