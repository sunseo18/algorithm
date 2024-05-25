import sys

t = int(sys.stdin.readline())

for i in range(t):
    n, m = map(int, sys.stdin.readline().split())

    
    A = list(map(int, sys.stdin.readline().split()))
    B = list(map(int, sys.stdin.readline().split()))

    
    A.sort()
    B.sort()
    b_length = len(B)

    sum = 0
    for a in A:
        if B[-1] < a:
            sum += b_length
        else:
            for i in range(b_length):
                if B[i] >= a:
                    if i == 0:
                        break
                    sum += (i)
                    break

            
    sys.stdout.write(str(sum))
    sys.stdout.write('\n')
