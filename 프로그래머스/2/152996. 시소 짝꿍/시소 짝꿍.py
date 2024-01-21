from itertools import combinations
from collections import Counter

def solution(weights):
    cnt = 0
    weights = Counter(weights)
    print(weights)
    for a, b in combinations(weights.keys(), 2): # 서로 다른 무게
        if a*2 == b*3 or a*2 == b*4 or a*3 == b*4 or b*2 == a*3 or b*2 == a*4 or b*3 == a*4:
            cnt += weights[a] * weights[b]
            print(cnt, weights[a], weights[b])
    for v in weights.values(): # 같은 무게
        if v > 1:
            cnt += sum([i for i in range(1, v)])
    return cnt
