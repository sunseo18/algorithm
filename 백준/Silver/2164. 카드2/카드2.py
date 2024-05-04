import sys
from collections import deque

n = int(sys.stdin.readline())

length = n
if n == 1:
    print(1)
    sys.exit()

queue = deque([i for i in range(1, n+1)])

while queue:
    queue.popleft()
    length -= 1

    if length == 1:
        print(queue[0])
        sys.exit()
        
    top = queue.popleft()
    queue.append(top)


    
