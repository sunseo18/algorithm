import sys
from itertools import combinations

n = int(sys.stdin.readline().strip())

stack = []
for i in range(n):
    a = int(sys.stdin.readline().strip())
    if a == 0:
        if stack:
            stack.pop()
    else:
        stack.append(a)
    

print(sum(stack))

