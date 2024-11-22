import sys
import heapq

input = sys.stdin.readline

n = int(input())

numbers = []

for _ in range(n):
    heapq.heappush(numbers, int(input()))

    
if n == 1:
    print(0)
    sys.exit()

if n == 2:
    print(sum(numbers))
    sys.exit()


else:
    _sum = 0

    while len(numbers) != 1:
        a = heapq.heappop(numbers)
        b = heapq.heappop(numbers)

        _sum += a+b

        heapq.heappush(numbers, a+b)

    
    
print(_sum)
