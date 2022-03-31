d = dict()
d[(0, 0, 0)] = 1

def solution(tup):
    a, b, c = tup[0], tup[1], tup[2]
    if a <= 0 or b <= 0 or c <= 0:
        a, b, c = 0, 0, 0
        tup = (a, b, c)
    elif a > 20 or b > 20 or c > 20:
        a, b, c = 20, 20, 20
        tup = (a, b, c)

    if tup in d:
        return d[tup]
    elif a < b < c:
        d[tup] = solution((a, b, c-1)) + solution((a, b-1, c-1)) - solution((a, b-1, c))
        return d[tup]
    else:
        d[tup] = solution((a-1, b, c)) + solution((a-1, b-1, c)) + solution((a-1, b, c-1)) - solution((a-1, b-1, c-1))
        return d[tup]
        
while True:
    t = tuple(map(int, input().split()))
    if t[0] == -1 and t[1] == -1 and t[2] == -1:
        break
    print(f"w({t[0]}, {t[1]}, {t[2]}) = {solution(t)}")



    