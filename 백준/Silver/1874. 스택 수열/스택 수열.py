import sys

n = int(sys.stdin.readline().strip())

target_array = []
for i in range(n):
    target_array.append(int(sys.stdin.readline().strip()))

no_array = [i for i in range(1, n+1)]

flag = False

stack = []
print_array = []
j = 0

for i in range(n):
    stack.append(no_array[i])
    print_array.append('+')
    
    cur = stack[-1]
    if cur == target_array[j]:
        stack.pop()
        print_array.append('-')

        j+=1
        
        if stack:
            while stack and stack[-1] == target_array[j]:
                stack.pop()
                print_array.append('-')
                j+=1

        if j == n:
            for p in print_array:
                sys.stdout.write(p)
                sys.stdout.write('\n')
            sys.exit()


if not flag:
    print('NO')

                
