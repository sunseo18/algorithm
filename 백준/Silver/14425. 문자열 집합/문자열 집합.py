from collections import defaultdict
N, M = map(int, input().split())
count = 0

alpha_dict = defaultdict(list)

for i in range(N):
    newWord = input()
    alpha_dict[newWord[0]].append(newWord)

for i in range(M):
    newMWord = input()
    if newMWord in alpha_dict[newMWord[0]]:
        count += 1

print(count)
