def checkIsOdd(num):
    if (num % 2 == 0):
        return False
    return True

def solution(num):
    
    answer = 0
    if checkIsOdd(num):
        answer = "Odd"
        
    else:
        answer = "Even"
    
    return answer
