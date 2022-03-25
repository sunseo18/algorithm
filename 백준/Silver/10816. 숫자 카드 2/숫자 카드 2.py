import bisect
import sys
n = int(sys.stdin.readline())
sangeun = list(map(int, sys.stdin.readline().split()))
sangeun.sort()
m = int(input())
card = list(map(int, sys.stdin.readline().split()))

for c in card:
    print(bisect.bisect_right(sangeun, c) - bisect.bisect_left(sangeun, c), end=" ")