import sys

n = int(sys.stdin.readline().strip())

no_array = list(map(int, sys.stdin.readline().strip().split()))
budget = int(sys.stdin.readline().strip())

length = 0
max = -1
for b in no_array:
    if b > max:
        max = b
    length += 1
    
start = 0
end = max


def possible(highest):
    total = 0
    for i in range(length):
        if no_array[i] <= highest:
            total += no_array[i]
        else:
            total += highest

        if total > budget:
            return False
    return True

while start <= end:
    mid = (start + end) // 2

    if not possible(mid):
        end = mid - 1

    else:
        start = mid + 1

print(end)
