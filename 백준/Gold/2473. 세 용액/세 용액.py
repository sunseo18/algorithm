import sys

input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))


numbers.sort()



_min = 3000000001

for start in range(0, n-2):
    middle = start + 1
    end = n-1
    while middle < end:
        tmp = numbers[start] + numbers[middle] + numbers[end]

        if abs(tmp) < _min:
            start_answer = numbers[start]
            middle_answer = numbers[middle]
            end_answer = numbers[end]
            _min = abs(tmp)

        if tmp == 0:
            print(numbers[start], numbers[middle], numbers[end])
            sys.exit()

        elif tmp > 0:
            tmp -= numbers[end]
            end -= 1

        else:
            tmp -= numbers[middle]
            middle += 1


print(start_answer, middle_answer, end_answer)
    
