import sys
n = int(sys.stdin.readline())

numbers = [0] * n
frequency = dict()
for i in range(n):
    inputno = int(sys.stdin.readline())
    numbers[i] = inputno

    #dictionary에 있으면 +1 없으면 0으로 저장
    if inputno in frequency:
        frequency[inputno] += 1
    else:
        frequency[inputno] = 1

#산술평균
mean = round(sum(numbers) / n)
print(mean)
#중앙값
middle = sorted(numbers)[round((n-1)/2)]
print(middle)
#최빈값
tmp = [x for x in frequency if frequency[x] == max(frequency.values())]
if len(tmp) == 1:
    print(tmp[0])
else:
    print(sorted(tmp)[1])
#범위
scope = max(numbers) - min(numbers)
print(scope)