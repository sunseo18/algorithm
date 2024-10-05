import sys

input = sys.stdin.readline


numbers = map(int, input().split())

print(*sorted(numbers))
