import sys
n = int(sys.stdin.readline())
list1 = map(int, sys.stdin.readline().split())

m = int(input())
list2 = map(int, sys.stdin.readline().split())

listset = set(list1)
for l in list2:
    if l in listset:
        print(1)
    else:
        print(0)