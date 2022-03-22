import sys
n = int(sys.stdin.readline())

no = list()
for _ in range(n):
    no.append(int(sys.stdin.readline()))

no.sort()

for i in range(len(no)):
    print(no[i])