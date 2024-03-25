n, k = map(int, input().split())

mother = 1
def factorial(n):
    if n == 2:
        return 2
    elif n == 1:
        return 1
    return n * factorial(n-1)

for i in range(k):
    mother *= n
    n -= 1

if k != 0:
    print(mother//factorial(k))
else:
    print(1)
