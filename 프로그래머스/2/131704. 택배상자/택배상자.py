def solution(order):
    length = len(order)
    result = 0
    box = [0] * length
    
    i = 1
    for o in order:
        box[o-1] = i
        i+=1
    stack = []
    
    i = 1
    for b in box:
        if b == i:
            result = i
            i += 1
            while stack:
                if stack[-1] == i:
                    stack.pop()
                    result = i
                    i += 1
                else:
                    break
        else:
            stack.append(b)
    
    return result