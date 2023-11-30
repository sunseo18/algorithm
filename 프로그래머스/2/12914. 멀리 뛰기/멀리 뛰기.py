def factorial(n):
    answer = 1
    for i in range(1, n+1):
        answer *= i
    return answer

def solution(n):
    answer = 1
    
    if n == 1:
        return answer 
    

    for j in range(1, (n//2)+1):
        i = n - (j*2)
        print(i, j)
        if i == 0 or j == 0:
            answer += 1
            return answer % 1234567
        answer += factorial(i+j) // (factorial(i) * factorial(j))

    return answer % 1234567