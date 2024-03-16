from itertools import combinations

n, m = list(map(int, input().split()))
cards = list(map(int, input().split()))

max = -1
for c in combinations([i for i in range(n)], 3):
    tmp = cards[c[0]] + cards[c[1]] + cards[c[2]]
    if tmp <= m and tmp >= max:
        max = tmp
        
print(max)