import sys
n, c = map(int, sys.stdin.readline().split())
houses = [0]*n
for i in range(n):
    houses[i] = int(sys.stdin.readline())
houses.sort()
start = 1
end = (max(houses) - min(houses) +1) // (c - 1)

result = 0
while start <= end:
    mid = (start + end)//2

    curr_house = houses[0]
    count = 1
    for i in range(1, len(houses)):
        if houses[i] - curr_house >= mid:
            count += 1
            curr_house = houses[i]
    
    if count < c:
        end = mid - 1
    else:
        result = mid
        start = mid + 1
    
print(result)
    