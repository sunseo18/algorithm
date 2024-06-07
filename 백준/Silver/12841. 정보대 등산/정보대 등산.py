import sys

n = int(sys.stdin.readline().strip())

cross_list = list(map(int, sys.stdin.readline().strip().split()))
left_list = list(map(int, sys.stdin.readline().strip().split()))
right_list = list(map(int, sys.stdin.readline().strip().split()))

cross_n = 0

answer_list = [0 for _ in range(n)]

answer_list[0] = cross_list[0]

for i in range(1, n-1):
    left_list[i] += left_list[i-1]

for i in range(1, n):
    crossed_weight = left_list[i-1] + cross_list[i]
    already_crossed_weight = answer_list[i-1] + right_list[i-1]
    
    answer_list[i] = min(already_crossed_weight, crossed_weight)

    if answer_list[i] == crossed_weight:
        if answer_list[i] == already_crossed_weight:
            continue
        else:
            cross_n = i

print(cross_n+1, answer_list[n-1])
