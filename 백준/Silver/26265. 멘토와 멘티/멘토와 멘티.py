import sys


n = int(sys.stdin.readline().strip())


pairs = []
for i in range(n):
    pairs.append(tuple(sys.stdin.readline().strip().split()))

pairs.sort(key = lambda t : t[1], reverse = True)
pairs.sort(key = lambda t : t[0])

for pair in pairs:
    sys.stdout.write(pair[0])
    sys.stdout.write(' ')
    sys.stdout.write(pair[1])
    sys.stdout.write('\n')
