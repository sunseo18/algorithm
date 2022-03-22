n = int(input())

no = list()
for _ in range(n):
    no.append(int(input()))

no.sort()

for i in range(len(no)):
    print(no[i])