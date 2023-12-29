def solution(A, B):
    
    length = len(A)
    before = A
    
    for i in range(length):
        if before == B:
            return i
        
        before = before[-1] + before[0:-1]
        
    
    return -1