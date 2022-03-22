import sys
n = int(sys.stdin.readline())
sortlist = [0] * 10001

for _ in range(n):
    sortlist[int(sys.stdin.readline())] += 1

for i in range(10001):
    if sortlist[i] != 0:
        for _ in range(sortlist[i]):
            print(i)

