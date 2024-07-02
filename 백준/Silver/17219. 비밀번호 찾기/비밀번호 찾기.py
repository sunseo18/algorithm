import sys

n, m = map(int, sys.stdin.readline().strip().split())


dictionary = dict()

for i in range(n):
    site, pwd = sys.stdin.readline().strip().split()

    dictionary[site] = pwd

for i in range(m):
    site = sys.stdin.readline().strip()
    sys.stdout.write(dictionary[site])
    sys.stdout.write('\n')
    
