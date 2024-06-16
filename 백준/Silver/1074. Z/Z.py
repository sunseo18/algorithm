import sys

n, r, c = map(int, sys.stdin.readline().strip().split())

min_answer = 0

a, b = 0, 0

n = 2**n
while n != 1:
    n = n//2

    if r < n:
        if c < n:
            pass
        else:
            min_answer += n*n
            c -= n
    else:
        if c < n:
            min_answer += n*n*2
            r -= n
        else:
            min_answer += n*n*3
            c -= n
            r -= n
    
    
print(min_answer)
