import sys
input = sys.stdin.readline

n = int(input())


line = list(map(int, input().split()))

for i in range(3):
    line[i] = (line[i], line[i])

for _ in range(n-1):
    new_line = list(map(int, input().split()))
    

    first = ( min(line[0][0], line[1][0]) + new_line[0], max(line[0][1], line[1][1]) + new_line[0] )     
    second = ( min(line[0][0], line[1][0], line[2][0]) + new_line[1], max(line[0][1], line[1][1], line[2][1]) + new_line[1] )
    third = ( min(line[1][0], line[2][0]) + new_line[2], max(line[1][1], line[2][1]) + new_line[2] )


    line[0], line[1], line[2] = first, second, third


print(max(line[0][1], line[1][1], line[2][1]), min(line[0][0], line[1][0], line[2][0]))
