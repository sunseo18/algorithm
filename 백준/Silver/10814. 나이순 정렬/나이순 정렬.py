import sys
n = int(sys.stdin.readline())

people = [0] * n
for i in range(n):
    age, name = sys.stdin.readline().split()
    people[i] = (int(age), name)

for p in sorted(people, key=lambda p: p[0]):
    print(p[0], p[1])