t = int(input())
l = [0] * t
for i in range(t):
    l[i] = int(input())

d = [0] * 41
d[0] = (1, 0)
d[1] = (0, 1)

maxn = max(l)

for i in range(2, maxn+1):
    d[i] = (d[i-2][0] + d[i-1][0], d[i-2][1] + d[i-1][1])

for number in l:
    print(d[number][0], d[number][1])

