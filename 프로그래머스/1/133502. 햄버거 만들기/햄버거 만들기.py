       
def solution(ingredient):
    answer = 0
    stack = []
    j = 0
    
    for i in ingredient:
        j += 1
        stack.append(i)      
        
        if j > 3:
            if stack[-4:] == [1, 2, 3, 1]:
                answer += 1
                stack.pop()
                stack.pop()
                stack.pop()
                stack.pop()
        
    return answer
