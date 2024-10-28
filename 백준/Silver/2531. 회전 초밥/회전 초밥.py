import sys

n, d, k, c = map(int, sys.stdin.readline().split())


sushi = []
for i in range(n):
    sushi.append(int(sys.stdin.readline().strip()))

sushi_dict = dict()

window_kind = 0
answer = 0


# 시작
i = 0
j = k-1

for x in range(i, j+1):
    if sushi[x] not in sushi_dict:
        sushi_dict[sushi[x]] = 1
        window_kind += 1
    else:
        sushi_dict[sushi[x]] += 1

if c not in sushi_dict:
    answer = window_kind + 1
else:
    answer = window_kind

while i < n-1:
    if sushi_dict[sushi[i]] == 1:
        sushi_dict[sushi[i]] -= 1
        window_kind -= 1
    else:
        sushi_dict[sushi[i]] -= 1

    i += 1

    j = (i+k-1) % n

    if sushi[j] in sushi_dict:
        if sushi_dict[sushi[j]] > 0:
            sushi_dict[sushi[j]] += 1
        else:
            sushi_dict[sushi[j]] += 1
            window_kind += 1
    else:
        sushi_dict[sushi[j]] = 1
        window_kind += 1

    # 쿠폰 검사
    if c not in sushi_dict or sushi_dict[c] == 0:
        answer = max(window_kind + 1, answer)
    else:
        answer = max(window_kind, answer)


print(answer)
    
