import sys
from collections import defaultdict

group, question = map(int, sys.stdin.readline().strip().split())


group_dict = defaultdict(list)
member_dict = dict()

for i in range(group):
    group = sys.stdin.readline().strip()

    member_no = int(sys.stdin.readline().strip())
    for j in range(member_no):
        member = sys.stdin.readline().strip()
        group_dict[group].append(member)
        member_dict[member] = group


for i in range(question):
    name = sys.stdin.readline().strip()
    type = int(sys.stdin.readline().strip())

    if type == 0:
        for member in sorted(group_dict[name]):
            sys.stdout.write(member)
            sys.stdout.write('\n')
    else:
        sys.stdout.write(member_dict[name])
        sys.stdout.write('\n')
