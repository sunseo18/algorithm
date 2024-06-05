import sys

n = int(sys.stdin.readline().strip())
stduent_list = list(map(int, sys.stdin.readline().strip().split()))
t, p = map(int, sys.stdin.readline().strip().split())

tshirt = 0

for student in stduent_list:
    if student % t != 0:
        tshirt += student//t + 1
    else:
        tshirt += student//t


max_pen = n//p
one_pen = n%p


print(tshirt)
print(max_pen, one_pen)
