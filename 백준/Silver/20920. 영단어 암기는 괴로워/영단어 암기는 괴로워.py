from collections import defaultdict
import sys

n, m = map(int, input().split())

word_dic = defaultdict(list)
no_word_dic = defaultdict(bool)

for _ in range(n):
    word = sys.stdin.readline().strip()

    if no_word_dic[word]:
        continue
    else:
        if len(word) < m:
            no_word_dic[word] = True
            continue


    if not word_dic[word]:
        word_dic[word] = [-1, -len(word)]
    else:
        word_dic[word][0] -= 1


for s in sorted(list(word_dic), key = lambda x : word_dic[x]+[x]):
    sys.stdout.write(s)
    sys.stdout.write('\n')

