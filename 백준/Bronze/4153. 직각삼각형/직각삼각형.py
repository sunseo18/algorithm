import sys

while True:
    lengthList = list(map(int, sys.stdin.readline().strip().split()))

    if lengthList[0] == 0 and lengthList[1] == 0 and lengthList[2] == 0:
        break

    lengthList.sort()

    if lengthList[0] ** 2 + lengthList[1] ** 2 == lengthList[2] ** 2:
        sys.stdout.write("right")
    else:
        sys.stdout.write("wrong")
    sys.stdout.write('\n')
