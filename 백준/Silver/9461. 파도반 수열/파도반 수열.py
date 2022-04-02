import sys
n = int(input())
nlist = [0] * n
for i in range(n):
    nlist[i] = int(sys.stdin.readline())

maxn = max(nlist)
array = [0] * max(7, maxn+1)
array[1] = 1
array[2] = 1
array[3] = 1
array[4] = 2
array[5] = 2
array[6] = 3
for i in range(7, maxn+1):
    array[i] = array[i-5] + array[i-1]

for n in nlist:
    print(array[n])
