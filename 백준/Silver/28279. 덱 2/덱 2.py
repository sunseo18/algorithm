from collections import deque
import sys

N = int(input())

deque = deque()
for _ in range(N):
    input_str = sys.stdin.readline().strip()
    input_no = list(map(int, input_str.split()))

    if input_no[0] == 1:
        deque.appendleft(input_no[1])

    elif input_no[0] == 2:
        deque.append(input_no[1])

    elif input_no[0] == 3:
        if deque:
            sys.stdout.write(str(deque.popleft()))
        else:
            sys.stdout.write('-1')
        sys.stdout.write('\n')

    elif input_no[0] == 4:
        if deque:
            sys.stdout.write(str(deque.pop()))
        else:
            sys.stdout.write('-1')
        sys.stdout.write('\n')

    elif input_no[0] ==5:
        sys.stdout.write(str(len(deque)))
        sys.stdout.write('\n')
    elif input_no[0] == 6:
        if not deque:
            sys.stdout.write('1')
        else:
            sys.stdout.write('0')
        sys.stdout.write('\n')

    elif input_no[0] == 7:
        if deque:
            sys.stdout.write(str(deque[0]))
        else:
            sys.stdout.write('-1')
        sys.stdout.write('\n')

    elif input_no[0] == 8:
        if deque:
            sys.stdout.write(str(deque[-1]))
        else:
            sys.stdout.write('-1')
        sys.stdout.write('\n')
        
    
