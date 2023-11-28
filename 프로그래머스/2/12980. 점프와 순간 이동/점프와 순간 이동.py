def solution(n):
    ans = 0
    
    if n == 1:
        return 1
    
    while n > 0:
        나머지 = n % 2
        if n % 2 > 0:
            n = n // 2
            ans += 1
            if n == 1:
                break
        elif n % 2 == 0:
            if n == 2:
                break
            n = n // 2

        
    return ans+1