import sys

sys.setrecursionlimit(10**5)
input = sys.stdin.readline

moeum = ['a', 'e', 'i', 'o', 'u']

jamo_dict = {'ja': 0, 'mo': 0}

L, C = map(int, input().split())
word = list(input().split())

C = len(word)
word.sort()
def dfs(tmp, depth):
    if depth == L:
        if jamo_dict['mo'] >= 1 and jamo_dict['ja'] >= 2:
            print("".join(tmp))
        return
    if depth == 0:  
        for i in range(depth, C):
            tmp[depth] = word[i]

            if word[i] in moeum:
                jamo_dict['mo'] += 1
            else:
                jamo_dict['ja'] += 1

            dfs(tmp, depth + 1)
                
            if tmp[depth] in moeum:
                jamo_dict['mo'] -= 1
            else:
                jamo_dict['ja'] -= 1
            tmp[depth] = ''
    else:
        for j in range(C):
            if word[j] > tmp[depth-1]:
                tmp[depth] = word[j]

                if word[j] in moeum:
                    jamo_dict['mo'] += 1
                else:
                    jamo_dict['ja'] += 1

                dfs(tmp, depth + 1)
                    
                if tmp[depth] in moeum:
                    jamo_dict['mo'] -= 1
                else:
                    jamo_dict['ja'] -= 1

                tmp[depth] = ''

dfs(['' for _ in range(L)], 0)
