import sys
import heapq


n = int(sys.stdin.readline().strip())

array = []

for i in range(n):
    no = int(sys.stdin.readline().strip())

    if no == 0:
        if not array:
            sys.stdout.write('0')
            sys.stdout.write('\n')

            continue
        sys.stdout.write(str(heapq.heappop(array)[1]))
        sys.stdout.write('\n')

        continue
    
    heapq.heappush(array, (abs(no), no))

