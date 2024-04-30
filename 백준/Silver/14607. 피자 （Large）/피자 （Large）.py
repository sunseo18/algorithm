import sys

N = int(sys.stdin.readline())

answer = N//2
if N % 2 != 0:
    answer *= ( ( N+1 ) // 2 + ((N+1)//2 -1))

else:
    answer *= ((N//2) + (N//2 -1 ))

print(answer)
