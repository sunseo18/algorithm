N = int(input())

def calc(n):
    answer = 0
    NCopy = n
    
    while NCopy > 0:
        answer += NCopy % 10
        NCopy //= 10
    return answer + n

answer = 0
for n in range(N+1):
    if calc(n) == N:
        answer = n
        break
        
print(answer)

