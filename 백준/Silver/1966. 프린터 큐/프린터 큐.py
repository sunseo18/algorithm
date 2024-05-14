import sys
from collections import deque

t = int(sys.stdin.readline().strip())


for i in range(t):
    n, m = map(int, sys.stdin.readline().strip().split())

    importance_array = list(map(int, sys.stdin.readline().strip().split()))
    
    index_importance_queue = deque([(i, importance_array[i]) for i in range(n)])

    importance_array = sorted(importance_array)



    print_no = 0
    while index_importance_queue:
        cur_index, cur_importance = index_importance_queue.popleft()

        if cur_importance < importance_array[-1]:
            index_importance_queue.append((cur_index, cur_importance))

        elif cur_importance == importance_array[-1]:
            print_no += 1
            importance_array.pop()

            if cur_index == m:
                sys.stdout.write(str(print_no))
                sys.stdout.write('\n')
                break
        

                
