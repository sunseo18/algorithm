import sys

n = int(sys.stdin.readline().strip())

lightArray = list(map(int, sys.stdin.readline().strip().split()))


def change(array, index):
    if array[index] == 1:
        array[index] = 0

    else:
        array[index] = 1
        
m = int(sys.stdin.readline().strip())

for i in range(m):
    a, b = map(int, sys.stdin.readline().strip().split())
    b-=1
    
    if a == 1:
        for index in range(b, n, b+1):
            change(lightArray, index)
    else:
        change(lightArray, b)
        
        left = b - 0
        right = n - b - 1

        for offset in range(1, min(left,right) + 1):
            if lightArray[b-offset] == lightArray[b+offset]:
                change(lightArray, b-offset)
                change(lightArray, b+offset)
            else:
                break

for i in range(n):
    sys.stdout.write(str(lightArray[i]))
    sys.stdout.write(' ')
    if (i+1) % 20 == 0:
        sys.stdout.write('\n')
        
                
            
