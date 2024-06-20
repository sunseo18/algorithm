import sys
from collections import deque

n = int(sys.stdin.readline().strip())

for _ in range(n):
    command = sys.stdin.readline().strip()

    length = int(sys.stdin.readline().strip())

    numbers = sys.stdin.readline().strip()[1:-1]
    if numbers == '':
        number_list= []
    else:
        number_list = deque(numbers.split(','))



    command = command.replace("RR", "")

    flag = 'f'
    break_flag = False
    for c in command:
        if c == 'R':
            if flag == 'f':
                flag = 'b'
            else:
                flag = 'f'

        elif c == 'D':
            if not number_list:
                print('error')
                break_flag = True
                break
            if flag == 'f':
                number_list.popleft()
                length -= 1
            elif flag == 'b':
                number_list.pop()
                length -= 1

    if not break_flag:
        sys.stdout.write('[')
        if flag == 'f':
            for i in range(length):
                sys.stdout.write(number_list[i])
                if i != length-1:
                    sys.stdout.write(',')
        else:
            for i in range(length-1, -1, -1):
                sys.stdout.write(number_list[i])
                if i != 0:
                    sys.stdout.write(',')
        sys.stdout.write(']')
        sys.stdout.write('\n')
    
