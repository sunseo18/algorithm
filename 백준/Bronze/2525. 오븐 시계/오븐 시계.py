import sys

a, b = map(int, sys.stdin.readline().strip().split())
c = int(sys.stdin.readline().strip())


new_minute = b + c

plus_hour = 0
while new_minute >= 60:
    new_minute -= 60
    plus_hour += 1

new_hour = a +plus_hour

while new_hour >= 24:
    new_hour -= 24


print(new_hour, new_minute)


