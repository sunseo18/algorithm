import sys

def maxMod(a, b):
    tmp = a % b
    if tmp == 0:
        return b

    return maxMod(b, tmp)

t = int(sys.stdin.readline().strip())

for i in range(t):
    n, m = map(int, sys.stdin.readline().strip().split())

    sys.stdout.write(str(n*m // maxMod(n, m)))
    sys.stdout.write('\n')

