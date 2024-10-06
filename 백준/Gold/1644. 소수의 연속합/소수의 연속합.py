import sys

input = sys.stdin.readline
N = int(input())
 
MAX = 4000000
sosu = [False, False] + [True] * (MAX-1)

for i in range(2, MAX+1):
    if sosu[i]:
        for j in range(2*i, MAX+1, i):
            sosu[j] = False

sosu_list = [0]

for i in range(1, MAX+1):
    if sosu[i]:
        sosu_list.append(i)

       
    



answer = 0
i, j = 0, 0

sosu_length = len(sosu_list)


tmp = sosu_list[i]
while i < sosu_length:
    if tmp == N:
        answer += 1
        j+= 1
        if j >= sosu_length:
            break
        tmp += sosu_list[j]
        
    elif tmp < N:
        j+=1
        if j >= sosu_length:
            break
        tmp += sosu_list[j]

    else:
        tmp -= sosu_list[i]
        i+=1


print(answer)

    
   