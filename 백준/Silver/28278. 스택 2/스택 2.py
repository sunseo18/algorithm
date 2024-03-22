import sys

N = int(sys.stdin.readline().rstrip())

stack = []
stack_len = 0

for _ in range(N):
    inputs = sys.stdin.readline().rstrip().split()
    if len(inputs) == 1:
        cmd = int(inputs[0])
        if cmd == 2:
            if stack_len != 0:
                sys.stdout.write(stack.pop())
                sys.stdout.write('\n')
                stack_len -= 1
            else:
                sys.stdout.write(str(-1))
                sys.stdout.write('\n') 
        elif cmd == 3:
            sys.stdout.write(str(stack_len))
            sys.stdout.write('\n') 
        elif cmd == 4:
            if stack_len == 0:
                sys.stdout.write('1\n')
            else:
                sys.stdout.write('0\n')
        elif cmd == 5:
            if stack_len != 0:
                sys.stdout.write(str(stack[-1]))
                sys.stdout.write('\n')    
            else:
                sys.stdout.write('-1')
                sys.stdout.write('\n') 

    else:
        stack.append(inputs[1])
        stack_len += 1
            
