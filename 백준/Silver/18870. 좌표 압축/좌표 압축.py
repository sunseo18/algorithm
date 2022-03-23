import sys

n = int(sys.stdin.readline())
inputs = list(map(int, sys.stdin.readline().split()))

points = sorted(set(inputs))

d = {points[i] : i for i in range(len(points))}

for i in inputs:
    print(d[i], end=" ")