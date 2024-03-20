MAX = 123456*2
arr = [i for i in range(MAX + 1)]

for i in range(2, MAX+1):
    if arr[i] == 0:
        continue
    for j in range(2*i, MAX+1, i):
        arr[j] = 0
    # i의 배수 index에 대한 배열 값을 모두 0으로 초기화

while True:
    n = int(input())
    if n == 0:
        break

    count = 0
    for i in range(n+1, 2*n+1):
        if arr[i] != 0:
            count += 1

    print(count)
