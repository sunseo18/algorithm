import sys

n, r, c = map(int, sys.stdin.readline().strip().split())

min_answer = 0

a, b = 0, 0

n = 2**n
while n != 1:
    half_n = n//2
    if a <= r < a+half_n:
        if b <= c < b+half_n:
            pass
        else:
            min_answer += n*n//4
            b += half_n
    else:
        if b <= c < b+n//2:
            min_answer += n*n//4*2
            a += half_n
        else:
            min_answer += (n*n//4)*3
            a += half_n
            b += half_n
            

    n = half_n
    
    
print(min_answer)
