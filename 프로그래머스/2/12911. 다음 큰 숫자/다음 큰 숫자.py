def solution(n):
    
    bin_n = str(bin(n))[2:]
    bin_n_1 = 0
    
    for b in bin_n:
        if b == '1':
           bin_n_1 += 1 
        
    next_n = n
    for i in range(10):
        next_n+=1
        bin_next_n = str(bin(next_n))[2:]
        bin_next_n_1 = 0
        
        for b in bin_next_n:
            if b == '1':
                bin_next_n_1 += 1

        if bin_n_1 == bin_next_n_1:
            return next_n

        
