import sys

l = int(sys.stdin.readline().strip())

word = sys.stdin.readline().strip()



answer = 0
i = 0
for w in word:
    no = ord(w)-96
    answer += no * (31**i)
    i+=1
print(answer % 1234567891)
