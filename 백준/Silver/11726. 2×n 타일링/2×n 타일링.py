import sys

answers = [0] * 1001
answers[0] = 0
answers[1] = 1
answers[2] = 2

n = int(sys.stdin.readline().strip())


for i in range(3, n+1):
    answers[i] = (answers[i-1] + answers[i-2]) % 10007

print(answers[n])
