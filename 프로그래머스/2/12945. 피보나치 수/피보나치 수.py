def fibo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    return fibo(n-1) + fibo(n-2)

def solution(n):
    fibo_array = [0] * 100001
    fibo_array[0] = 0
    fibo_array[1] = 1
    
    for i in range(2, n+1):
        fibo_array[i] = fibo_array[i-2] + fibo_array[i-1]
    
    answer = fibo_array[n] % 1234567
    return answer