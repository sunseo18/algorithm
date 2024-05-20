import sys
import heapq

heap = []

n = int(sys.stdin.readline().strip())


for i in range(n):
    input_no = int(sys.stdin.readline().strip())

    if input_no == 0:
        if not heap:
            print(0)
        else:
            print(-heapq.heappop(heap))

    else:
    
        heapq.heappush(heap, -input_no)

    
