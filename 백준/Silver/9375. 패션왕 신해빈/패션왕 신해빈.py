import sys
from collections import defaultdict

t = int(sys.stdin.readline().strip())

for _ in range(t):
    dictionary = defaultdict(int)

    n = int(sys.stdin.readline().strip())
    for i in range(n):
        dress, where = sys.stdin.readline().strip().split()

        dictionary[where] += 1


    total = 1
    for k in dictionary.keys():
        total *= ( dictionary[k] + 1 )

    sys.stdout.write(str(total-1))
    sys.stdout.write('\n')
