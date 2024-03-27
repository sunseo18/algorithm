from collections import defaultdict
import sys

n = int(input())

answer = 1

dic = defaultdict(bool)
dic['ChongChong'] = True

for _ in range(n):
    a, b = sys.stdin.readline().strip().split()

    if dic[a] == dic[b]:
        continue
    elif dic[a] and not dic[b]:
        answer += 1
        dic[b] = True

    else:
        answer += 1
        dic[a] = True

sys.stdout.write(str(answer))
