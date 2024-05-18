import sys

n = int(sys.stdin.readline().strip())
answer = 0
times = []
for i in range(n):
    times.append(list(map(int, sys.stdin.readline().strip().split())))

times.sort()

tmp = times[0][1]
answer = 1

for i in range(1, n):
    start, end = times[i]

    # 이전 거랑 겹치면 더 빨리 끝나는 걸로
    if start < tmp:
        tmp = min(end, tmp)

    # 안 겹치면 개수 늘리고 끝나는 시간 갱신
    else:
        answer += 1
        tmp = end
    
print(answer)
