import sys

input = sys.stdin.readline

n = int(input())

for _ in range(n):
    word = input().strip()
    print(word[0], end="")
    print(word[-1])
