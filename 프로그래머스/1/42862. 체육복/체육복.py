def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    
    i, max_i = 0, len(reserve)
    while i < max_i:
        same_no = reserve[i]
        if same_no in lost:
            lost.remove(same_no)
            reserve.remove(same_no)
            max_i -= 1
        else:
            i+=1
        
    answer = n - (len(lost) + len(reserve))
    
    for r in reserve:
        for l in lost:
            if l == r-1 or l == r+1:
                lost.remove(l)
                answer += 1
                break 
                
    answer += len(reserve)
    
                
    return answer