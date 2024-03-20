def is_sosu(x):
    if x == 0 or x == 1:
        return False
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True
    

M, N = map(int, input().split())
for x in range(M, N+1):
    if is_sosu(x):
        print(x)
