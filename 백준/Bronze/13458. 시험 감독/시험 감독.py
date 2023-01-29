N = int(input())
A = list(map(int, input().split()))
B, C = list(map(int, input().split()))

answer = N
for a in A:
    a -= B
    if a > 0:
        if a % C:
            answer += (a // C) + 1
        else:
            answer += (a // C)

print(answer)