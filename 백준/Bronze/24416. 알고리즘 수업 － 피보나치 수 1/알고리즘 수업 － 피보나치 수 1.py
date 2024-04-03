N = int(input())
fibList = [0]*(N+1)
number = 0

def fib(n):
    for i in range(1, n+1):
        if i == 1 or i == 2:
            fibList[i] = 1
        else:
            fibList[i] = fibList[i-1] + fibList[i-2]


fib(N)
print(fibList[N], N-2)

