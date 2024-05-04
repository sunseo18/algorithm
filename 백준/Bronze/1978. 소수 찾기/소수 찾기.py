import sys

n = int(sys.stdin.readline())

numbers = list(map(int, sys.stdin.readline().strip().split()))

sosu = n

for no in numbers:
    if no == 0 or no == 1:
        sosu -= 1
    for i in range(2, int(no**0.5)+1):
        if no % i == 0:
            sosu -= 1
            break
print(sosu)
