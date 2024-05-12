import sys

n, m = map(int, sys.stdin.readline().strip().split())

no_array = list(map(int, sys.stdin.readline().strip().split()))

sum = 0
for i in range(n):
    sum += no_array[i]

start = sum // m
end = sum

def possible(limit):
    global m
    chop = 1
    tmp = 0
    for no in no_array:
        if tmp + no > limit:
            chop += 1
            tmp = no
            if tmp > limit:
                return False
        else:
            tmp += no

        if chop > m:
            return False
    if chop <= m:
        return True
    else:
        return False

while start < end:
    mid = (start + end) // 2

    if not possible(mid):
        start = mid + 1
    else:
        end = mid

print(start)
