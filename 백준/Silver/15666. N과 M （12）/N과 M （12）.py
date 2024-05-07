import sys

n, m = map(int, sys.stdin.readline().strip().split())

no_array = list(set(map(int, sys.stdin.readline().strip().split())))

array_length = len(no_array)

no_array.sort()

def dfs(tmp, start, depth):
    if start == depth:
        for t in tmp:
            sys.stdout.write(str(t))
            sys.stdout.write(" ")
        sys.stdout.write('\n')
        return

    for no in no_array:
        if start >= 1:
            if no < tmp[start-1]:
                continue
        tmp[start] = no
        dfs(tmp, start+1, depth)
        

dfs([0]*m, 0, m)
