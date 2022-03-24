number = int(input())
def star(n, shape):
    if n > number:
        for r in shape:
            print(r)
        return
    
    tmp = []
    for i in range(n//3):
        tmp.append(shape[i]*3)
    for i in range(n//3):
        tmp.append(shape[i] + ' '*(n//3) + shape[i])
    for i in range(n//3):
        tmp.append(shape[i]*3)

    star(n*3, tmp)
    
star(3, ['*'])