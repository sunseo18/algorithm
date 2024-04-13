import sys

word = sys.stdin.readline().strip()
q = int(sys.stdin.readline().strip())
alpha = [[0] * 26]
length = len(word)

for i in range(length):
    if i == 0:
       alpha[-1][ord(word[i])-97] += 1
    else:
        alpha.append(alpha[-1][:])
        alpha[-1][ord(word[i])-97] += 1

for i in range(q):
    a, l, r = sys.stdin.readline().strip().split()

    l, r = int(l), int(r)
    
    if l == 0:
        sys.stdout.write(str(alpha[r][ord(a)-97]))

    else:
        sys.stdout.write(str(alpha[r][ord(a)-97] - alpha[l-1][ord(a)-97]))

    sys.stdout.write('\n')

