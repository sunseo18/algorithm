T = int(input())

numbers = []
for _ in range(T):
    numbers.append(map(int, input().split()))

def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)
        
for i in range(T):
    A, B = numbers[i]
    
    tmp = gcd(A, B)
    print( A * B // tmp)
