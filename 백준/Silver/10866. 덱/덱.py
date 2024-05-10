import sys
from collections import deque

queue = deque()
length = 0

n = int(sys.stdin.readline().strip())

for _ in range(n):
    input = sys.stdin.readline().strip().split()
    command = input[0]
    if command == 'push_front':
        number = int(input[1])
        queue.appendleft(number)
        length += 1

    elif command == 'push_back':
        number = int(input[1])
        queue.append(number)
        length += 1

    elif command == 'pop_front':
        if length == 0:
            sys.stdout.write('-1')
        else:
            sys.stdout.write(str(queue.popleft()))
            length -= 1
        sys.stdout.write('\n')

    elif command == 'pop_back':
        if length == 0:
            sys.stdout.write('-1')
        else:
            sys.stdout.write(str(queue.pop()))
            length -= 1
        sys.stdout.write('\n')

    elif command == 'size':
        sys.stdout.write(str(length))
        sys.stdout.write('\n')
    elif command == 'empty':
        if length == 0:
            sys.stdout.write('1')
        else:
            sys.stdout.write('0')
        sys.stdout.write('\n')
    elif command == 'front':
        if length == 0:
            sys.stdout.write('-1')
        else:
            sys.stdout.write(str(queue[0]))
        sys.stdout.write('\n')

    elif command == 'back':
        if length == 0:
            sys.stdout.write('-1')
        else:
            sys.stdout.write(str(queue[-1]))
        sys.stdout.write('\n')

