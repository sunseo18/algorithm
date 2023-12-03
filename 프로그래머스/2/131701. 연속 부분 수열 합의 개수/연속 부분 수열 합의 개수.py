def solution(elements):
    
    s = set()
    length = len(elements)
    
    for i in range(1, length):
        for j in range(length):
            
            if (j+i) >= length:
                end = (j + i) % length
                e = elements[j:] + elements[0: end]
            else: 
                e = elements[j: j+i]

            s.add(sum(e))

            
    s.add(sum(elements))
            
        
    return len(s)