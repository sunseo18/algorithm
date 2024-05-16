import sys

while True:
    sentance = sys.stdin.readline().rstrip()

    if sentance == '.':
        sys.exit()
        
    stack = []
    for s in sentance:
        if s == '(' or s == '[':
            stack.append(s)

        elif s == ')':
            if stack and stack[-1] == '(':
                stack.pop()
                continue
            stack.append(s)
            break
        elif s == ']':
            if stack and stack[-1] == '[':
                stack.pop()
                continue
            
            stack.append(s)
            break


    if stack:
        print('no')
    else:
        print('yes')
