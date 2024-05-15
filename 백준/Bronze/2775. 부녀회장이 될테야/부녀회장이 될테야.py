import sys

t = int(sys.stdin.readline().strip())

apart = [[i for i in range(15)]]
for i in range(1, 15):
    tmp = [0, 1]
    for j in range(2, 15):
        tmp.append(tmp[j-1] + apart[i-1][j])

    apart.append(tmp)

for i in range(t):
    k = int(sys.stdin.readline().strip())
    n = int(sys.stdin.readline().strip())

    sys.stdout.write(str(apart[k][n]))
    sys.stdout.write('\n')
