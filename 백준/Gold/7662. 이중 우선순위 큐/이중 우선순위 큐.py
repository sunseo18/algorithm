import sys
import heapq
from collections import defaultdict

t = int(sys.stdin.readline().strip())


for _ in range(t):
    k = int(sys.stdin.readline().strip())

    min_heap = []
    max_heap = []
    length = 0
    dictionary = defaultdict(int)

    for i in range(k):
        cmd, no = sys.stdin.readline().strip().split()
        no = int(no)
        
        
        if cmd == 'I':
            length += 1
            dictionary[no] += 1
            heapq.heappush(min_heap, no)
            heapq.heappush(max_heap, -no)

        if cmd == 'D':
            if length == 0:
                continue
            else:
                if no == -1:
                    while dictionary[min_heap[0]] == 0:
                        heapq.heappop(min_heap)
                    else:
                        popped_no = heapq.heappop(min_heap)
                        dictionary[popped_no] -= 1
                        length -= 1
                    
                if no == 1:
                    while dictionary[-max_heap[0]] == 0:
                        heapq.heappop(max_heap)
                    else:
                        popped_no = heapq.heappop(max_heap)
                        dictionary[-popped_no] -= 1
                        length -= 1
        
    if length == 0:
        sys.stdout.write('EMPTY')
        sys.stdout.write('\n')
        continue
    
    while dictionary[-max_heap[0]] == 0:
        heapq.heappop(max_heap)
    while dictionary[min_heap[0]] == 0:
        heapq.heappop(min_heap)
    sys.stdout.write(str(-heapq.heappop(max_heap)) + ' ')
    sys.stdout.write(str(heapq.heappop(min_heap)))
    sys.stdout.write('\n')
                    
