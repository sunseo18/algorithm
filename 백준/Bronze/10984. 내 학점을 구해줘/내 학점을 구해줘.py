T = int(input())
for _ in range(T):
    N = int(input())
    scores = [0] * N
    for i in range(N):
        scores[i] = tuple(map(eval, input().split()))

    time = 0
    score = 0
    for i in range(N):
        time += scores[i][0]
        score += (scores[i][1] * scores[i][0])
    print(time, round(score/time, 1))