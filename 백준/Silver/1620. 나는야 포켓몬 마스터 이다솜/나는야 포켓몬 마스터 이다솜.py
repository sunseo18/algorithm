import sys

n, m= map(int, sys.stdin.readline().strip().split())

poketmon_name = dict()
poketmon_number = dict()

for i in range(n):
    name = sys.stdin.readline().strip()

    poketmon_name[name] = i+1
    poketmon_number[i+1] = name
    
for i in range(m):
    question = sys.stdin.readline().strip()

    if question.isalpha():
        sys.stdout.write(str(poketmon_name[question]))
    else:
        sys.stdout.write(poketmon_number[int(question)])
    sys.stdout.write('\n')
