def solution(s):
    
    s_list = list(s)
    
    stack = []
    
    for s in s_list:
        if not stack:
            stack.append(s)
            
        elif stack:
            if s == ')':
                if stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(s)
            else:
                stack.append(s)
                    
                    
    if not stack:
        return True
    else:
        return False
