import sys

input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))


LIS = [numbers[0]]

def index(start, end, LIS, number):
    while start <= end:
        mid = (start + end ) // 2
        if LIS[mid] == number:
            return mid
        elif LIS[mid] > number:
            end = mid-1
        else:
            start = mid+1

    return start

for i in range(1, n):
    if LIS[-1] < numbers[i]:
        LIS.append(numbers[i])

    else:
        LIS[index(0, len(LIS)-1, LIS, numbers[i])] = numbers[i]

print(len(LIS))
