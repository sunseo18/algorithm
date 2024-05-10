import sys

n = int(sys.stdin.readline().strip())

fact = 1
for i in range(n, 0, -1):
    fact *= i


fact_str = str(fact)


zero_no = 0

for i in range(len(fact_str)-1, -1, -1):
    if fact_str[i] == '0':
        zero_no += 1
    if fact_str[i] != '0':
        print(zero_no)
        break
