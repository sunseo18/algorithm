N = int(input())

A = sorted(list(map(int, input().split())), reverse=True) # 큰 순서대로 
B = sorted(map(int, input().split())) # 작은 순서대로
sum = 0
for i in range(N):
    sum += A[i] * B[i]

print(sum)