N = int(input())
numbers = list(map(int, input().split()))

answer = min(numbers) * max(numbers)

print(answer)