import sys

n = int(sys.stdin.readline())
words = [0] * n

for i in range(n):
    word = sys.stdin.readline().rstrip()
    words[i] = (len(word), word)

words = list(set(words))

for t in sorted(words):
    print(t[1])
