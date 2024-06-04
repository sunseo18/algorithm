import sys
from collections import defaultdict

sys.setrecursionlimit(10000000)

count = 0
flag = False
output = ""

def dfs(w_list, length, w_dict, n, depth):
    global count
    global output
    global flag
    
    if depth == length:
        count += 1

        if count == n:
            output = "".join(word)
            flag = True

        return
        
    for i in range(length):
        if not w_dict[i]:
            word[depth] = w_list[i]
            w_dict[i] = True

            dfs(w_list, length, w_dict, n, depth+1)
            word[depth] = '0'
            w_dict[i] = False
            
while True:
    try: 
        input = sys.stdin.readline().strip().split()
        w_list = list(input[0])
        n = int(input[1])

        length = len(w_list)
        w_dict = defaultdict(bool)

        word = ['0' for _ in range(length)]

        count = 0
        flag = False
        output = ""
    
        dfs(w_list, length, w_dict, n, 0)

        if flag:
            sys.stdout.write("".join(w_list) + " " + str(n) + " = " + output)
        else:
            sys.stdout.write("".join(w_list) + " " + str(n) + " = " + "No permutation")
        sys.stdout.write('\n')

    except:
        break
