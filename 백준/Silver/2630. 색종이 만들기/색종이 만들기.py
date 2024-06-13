import sys
sys.setrecursionlimit(9999999)

k = int(sys.stdin.readline().strip())

array = []

for i in range(k):
    array.append(sys.stdin.readline().strip().split())


def check(iss, ib, js, jb, start):
    for i in range(iss, ib):
        for j in range(js, jb):
            if array[i][j] != start:
                return False
    return True

blue = 0
white = 0
def recurs(a, b, c, d, n):
    global blue
    global white
    if n == 1:
        if array[a][c] == '1':
            blue += 1
            return
        else:
            white += 1
            return

    start = array[a][c]
    if start == '1':
        if check(a, b, c, d, '1') == True:
            blue += 1
            return
    else:
        if check(a, b, c, d, '0') == True:
            white += 1
            return
    
    recurs(a, b-n//2, c, d-n//2, n//2)
    recurs(a, b-n//2, c+n//2, d, n//2)
    recurs(a+n//2, b, c, d-n//2, n//2)
    recurs(a+n//2, b, c+n//2, d, n//2)
    
            
        
recurs(0, k, 0, k, k)
print(white)
print(blue)
