import sys
from collections import defaultdict

n, m = map(int, sys.stdin.readline().strip().split())

no_array = sys.stdin.readline().strip().split()

array_length = len(no_array)
no_array.sort(key = lambda k : int(k))
array_dict = defaultdict(bool)

def dfs(tmp, start, depth):
    if start == depth:
        text = ''.join(tmp)
        if not array_dict[text]:
            for t in tmp:
                sys.stdout.write(t)
                sys.stdout.write(" ")
            sys.stdout.write('\n')
            array_dict[text] = True
        return

    for no in no_array:
        tmp[start] = no
        dfs(tmp, start+1, depth)
        


dfs([0]*m, 0, m)
