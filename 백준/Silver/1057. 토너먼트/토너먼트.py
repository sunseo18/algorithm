import sys

n, k, l = map(int, sys.stdin.readline().strip().split())
count = 0

while k != l:
    if k % 2 == 1:
        k = (k + 1)//2
    elif k % 2 == 0:
        k //= 2
        
    if l % 2 == 0:
        l //= 2
    elif l % 2 == 1:
        l = (l + 1)//2
    count += 1

print(count)
