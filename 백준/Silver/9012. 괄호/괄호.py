n = int(input())
for _ in range(n):
    vps = list(input())
    flag = False
    stack = []
    for v in vps:
        if v == '(':
            stack.append(v)
        else:
            if len(stack) == 0:
                flag = True 
                print('NO')
                break

            stack.pop()

    if stack:
        print('NO')
    elif not flag:
        print('YES')
