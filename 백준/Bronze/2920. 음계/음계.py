import sys

numbers = list(map(int, sys.stdin.readline().strip().split()))


ascending = True
descending = True

for i in range(1, len(numbers)):
    if numbers[i] < numbers[i-1]:
        ascending = False
    elif numbers[i] > numbers[i-1]:
        descending = False

if ascending:
    print("ascending")
elif descending:
    print("descending")
else:
    print("mixed")

