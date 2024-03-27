from collections import defaultdict
import sys

n = int(input())

answer = 0

for _ in range(n):
    s = sys.stdin.readline().strip()

    if s == 'ENTER':
        dic = defaultdict(bool)

    else:
        if not dic[s]:
            dic[s] = True
            answer += 1

sys.stdout.write(str(answer))
