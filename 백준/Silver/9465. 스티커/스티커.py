import sys

T = int(sys.stdin.readline().strip())

for i in range(T):
    n = int(sys.stdin.readline().strip())

    array = []

    for _ in range(2):
        array.append(list(map(int, sys.stdin.readline().strip().split())))

    if n > 1:
        array[0][1] += array[1][0] 
        array[1][1] += array[0][0]
    
    for i in range(2, n):
        array[0][i] += max(array[1][i-1], array[1][i-2])
        array[1][i] += max(array[0][i-1], array[0][i-2])
        
    sys.stdout.write(str(max(array[0][n-1], array[1][n-1])))
    sys.stdout.write('\n')

