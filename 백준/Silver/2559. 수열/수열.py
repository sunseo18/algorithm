import sys

n, k = map(int, sys.stdin.readline().strip().split())
arr = [0] + list(map(int, sys.stdin.readline().strip().split()))
arr2 = []
max = -100*n
    
for i in range(0, n+1):
    if i >= 1:
        arr[i] += arr[i-1]


    if i >= k:
        tmp = arr[i] - arr[i-k]
        if tmp > max:
            max = tmp

print(max)
