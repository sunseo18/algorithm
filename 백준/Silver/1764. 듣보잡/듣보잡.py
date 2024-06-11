import sys
from collections import defaultdict

n, m = map(int, sys.stdin.readline().strip().split())

never_heard = defaultdict(bool)
answer = []

for i in range(n):
    name = sys.stdin.readline().strip()
    never_heard[name] = True

number = 0

for i in range(m):
    name = sys.stdin.readline().strip()
    if never_heard[name]:
        number += 1
        answer.append(name)

sys.stdout.write(str(number) + '\n')
for name in sorted(answer):
    sys.stdout.write(name + '\n')

