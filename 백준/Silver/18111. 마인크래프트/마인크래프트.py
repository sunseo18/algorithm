import sys

n, m, b = map(int, sys.stdin.readline().strip().split())

maps = []

for i in range(n):
    maps.append(list(map(int, sys.stdin.readline().strip().split())))

max_height = -1
for i in range(n):
    for j in range(m):
        if maps[i][j] > max_height:
            max_height = maps[i][j]

            
def check(target, inventory):
    time = 0

    for i in range(n):
        for j in range(m):
            if maps[i][j] >= target:
                diff = maps[i][j] - target
                time += diff*2
                inventory += diff
            else:
                diff = target - maps[i][j]
                time += diff
                inventory -= diff

    if inventory < 0:
        return -1

    return time


target = max_height
answer_time = 99999999999
answer_target = -1

for t in range(0, target+1):
    tmp = check(t, b)
    if tmp < 0:
        break
    else:
        if tmp < answer_time:
            answer_time = tmp
            answer_target = t
        if tmp == answer_time:
            if t > answer_target:
                answer_target = t


print(answer_time, answer_target)
        
    
                
