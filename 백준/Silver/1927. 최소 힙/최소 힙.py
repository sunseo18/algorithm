import sys
import heapq

n = int(sys.stdin.readline().strip())

heap = []

for i in range(n):
    x = int(sys.stdin.readline().strip())
    if x == 0:
        if heap:
            sys.stdout.write(str(heapq.heappop(heap)))
        else:
            sys.stdout.write('0')
        sys.stdout.write('\n')
    else:
        heapq.heappush(heap, x)
    