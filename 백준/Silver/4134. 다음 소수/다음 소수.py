no = int(input())
MAX = 5_000_000_001

def is_sosu(x):  
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True
    
def next_sosu(n):
    if n == 0 or n == 1:
        return 2
    for x in range(n, MAX):
        if is_sosu(x):
            return x
    
for _ in range(no):
    n = int(input())

    print(next_sosu(n))

    
