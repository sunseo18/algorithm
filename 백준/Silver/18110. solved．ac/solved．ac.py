import math
import sys

def round(n):
    if n - int(n) >= 0.5:
        return math.ceil(n)
    else:
        return int(n)
    
n = int(sys.stdin.readline().strip())
if n == 0:
    print(0)
    sys.exit()

    
hard = []
for i in range(n):
    hard.append(int(sys.stdin.readline().strip()))

hard.sort()

not_include = round(n*0.15)

if not_include == 0:
    sys.stdout.write(str(round(sum(hard)/n)))
    sys.exit()

print(round(sum(hard[not_include:-not_include])/(n-not_include*2)))

