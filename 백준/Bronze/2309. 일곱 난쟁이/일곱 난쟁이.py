import sys
from itertools import combinations
NUM = 9
array = []
for i in range(NUM):
    array.append(int(sys.stdin.readline().strip()))

array.sort()

idexList = [i for i in range(9)]
combiList = combinations(idexList, 7)

for combi in combiList:
    sum = 0

    for c in combi:
        sum += array[c]

    if sum == 100:
        for c in combi:
            print(array[c], end="\n")
        break

