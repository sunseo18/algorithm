import sys

n = int(sys.stdin.readline().strip())

array = []

for i in range(n):
    array.append(list(map(int, sys.stdin.readline().strip().split())))

array.sort(key = lambda x : x[1], reverse = True)

tmp = array[0][1]

for i in range(n):
    ti, si = array[i]

    if tmp < si:
        tmp = tmp - ti

    else:
        tmp = si - ti

if tmp >= 0:
    print(tmp)

else:
    print(-1)
