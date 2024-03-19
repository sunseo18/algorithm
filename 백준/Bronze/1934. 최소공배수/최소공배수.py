T = int(input())

numbers = []
for _ in range(T):
    numbers.append(map(int, input().split()))

def gcd(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a
        
for i in range(T):
    A, B = numbers[i]
    
    tmp = gcd(A, B)
    print( A * B // tmp)
