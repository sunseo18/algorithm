import sys

n = int(sys.stdin.readline().strip())

apartment = []
for i in range(n):
    apartment.append(list(sys.stdin.readline().strip()))

di = [1, -1, 0, 0]
dj = [0, 0, -1, 1]

number = 0

def dfs(i, j):
    global apartment
    global number
        
    if apartment[i][j] == '0':
        return

    number += 1
    apartment[i][j] = '0'

    for d in range(4):
        next_i, next_j = i + di[d], j + dj[d]
        if 0 <= next_i < n and 0 <= next_j < n:
            dfs(next_i, next_j)


answer_list = []
for i in range(n):
    for j in range(n):
        number = 0
        dfs(i, j)
        if number != 0:
            answer_list.append(number)

sys.stdout.write(str(len(answer_list)) + '\n')
for a in sorted(answer_list):
    sys.stdout.write(str(a) + '\n')
