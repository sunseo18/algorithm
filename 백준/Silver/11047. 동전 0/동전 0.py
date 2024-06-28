import sys

n, k = map(int , sys.stdin.readline().strip().split())

array = []
length = 0
for _ in range(n):
    array.append(int(sys.stdin.readline().strip()))
    length += 1

answer = 0
for i in range(length -1, -1, -1):
    m = array[i]

    while m <= k:
        answer += k // m
        k %= m

print(answer)
