n = int(input())
for _ in range(n):
    vps = list(input())
    earlyReturn = False
    stack = []
    for v in vps:
        if v == '(':
            stack.append(v)
        else:
            if len(stack) == 0:
                earlyReturn = True 
                break

            stack.pop()

    if stack or earlyReturn:
        print('NO')
    else:
        print('YES')