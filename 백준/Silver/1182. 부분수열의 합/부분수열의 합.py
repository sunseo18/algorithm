import sys
import itertools

n, s = map(int, sys.stdin.readline().split())

numbers = list(map(int, sys.stdin.readline().split()))

answer = 0

for i in range(1, n+1):
    for c in itertools.combinations(numbers,i):
        if sum(c) == s:
            answer += 1


print(answer)
