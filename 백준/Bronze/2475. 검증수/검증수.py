import sys

numbers = map(int, sys.stdin.readline().strip().split())

answer = 0
for n in numbers:
    answer += n**2

print(answer %10)
