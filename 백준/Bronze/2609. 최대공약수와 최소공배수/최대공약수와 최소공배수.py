import sys

a, b = map(int, sys.stdin.readline().strip().split())

def hoje(a, b):
    if a % b == 0:
        return b

    else:
        return hoje(b, a%b)

min = hoje(a, b)
print(min)
print(a*b // min)
