import sys

input = sys.stdin.readline

n = int(input())

numbers = list(map(int, input().split()))

target = int(input())

sorted_no= sorted(numbers)

i= 0
j = n-1

answer = 0
while i < j:
    tmp = sorted_no[i] + sorted_no[j]


    if tmp == target:
        answer += 1
        i+=1
    elif tmp < target:
        i+=1
    else:
        j-=1

        

print(answer)
