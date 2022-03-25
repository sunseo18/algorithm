import sys
k, n = map(int, sys.stdin.readline().split())

lines = [0] * k
for i in range(k):
    lines[i] = int(sys.stdin.readline())

maximum = sum(lines)//n
def check(lines, length):
    result = 0
    for line in lines:
        result += line // length
    return result

def solution(start, end):
    global lines, maximum
    if start < end:
        return maximum

    mid = (start+end) //2
    if mid == 0:
         return 0
    if check(lines, mid) < n:
        return solution(mid-1, end)
    else:
        if check(lines, mid+1) < n:
            return mid
        else:
            return solution(start, mid+1)
    
print(solution(maximum, 1))