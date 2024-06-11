import sys
from collections import defaultdict

n = int(sys.stdin.readline().strip())

sett = set()

for i in range(n):
    inputs = sys.stdin.readline().strip().split()

    if inputs[0] == "add":
        sett.add(int(inputs[1]))

    elif inputs[0] == "remove":
        if int(inputs[1]) in sett:
            sett.remove(int(inputs[1]))

    elif inputs[0] == "check":
        if int(inputs[1]) in sett:
            print(1)
        else:
            print(0)

    elif inputs[0] == "toggle":
        if int(inputs[1]) in sett:
            sett.remove(int(inputs[1]))
        else:
            sett.add(int(inputs[1]))

    elif inputs[0] == "all":
        sett = {i for i in range(1, 21)}

    elif inputs[0] == "empty":
        sett = set()


