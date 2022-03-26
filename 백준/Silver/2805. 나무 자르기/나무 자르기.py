n, m = map(int, input().split())
trees = list(map(int, input().split()))

def check(trees, length):
    meter = 0
    for tree in trees:
        diff = tree - length
        if diff > 0:
            meter += diff
    return meter

def solution(trees, start, end):
    if start > end:
        return 0
    mid = (start + end) // 2
    if check(trees, mid) < m:
        return solution(trees, start, mid-1)
    else:
        if check(trees, mid+1) < m:
            return mid
        else:
            return solution(trees, mid+1, end)


print(solution(trees, 1, max(trees)))