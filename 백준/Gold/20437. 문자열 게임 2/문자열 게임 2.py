import sys
from collections import defaultdict


input = sys.stdin.readline

t = int(input())

min_length = 100001
max_length = 0
flag = False 
for _ in range(t):
    word = input()
    k = int(input())

    index_dictionary = defaultdict(list)
    count_dictionary = defaultdict(int)
    
    for i in range(len(word)):
        index_dictionary[word[i]].append(i)
        count_dictionary[word[i]] += 1

        if count_dictionary[word[i]] == k:
            flag = True
            min_length = min(min_length, i - index_dictionary[word[i]][0] + 1)
            max_length = max(max_length, i - index_dictionary[word[i]][0] + 1)

            index_dictionary[word[i]].pop(0)
            count_dictionary[word[i]] -= 1
    if flag:
        sys.stdout.write(str(min_length))
        sys.stdout.write(' ')
        sys.stdout.write(str(max_length))
    else:
        sys.stdout.write('-1')

    sys.stdout.write('\n')

    min_length = 100001
    max_length = 0
    flag = False
        
