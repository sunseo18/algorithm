import sys

first = sys.stdin.readline().strip()
second = sys.stdin.readline().strip()
third = sys.stdin.readline().strip()

if not first.isalpha():
    next = int(first) + 3
if not second.isalpha():
    next = int(second) + 2
if not third.isalpha():
    next = int(third) + 1


if next % 5 == 0 and next % 3 == 0:
    print("FizzBuzz")

elif next%5 == 0 and next % 3 != 0:
    print("Buzz")
    
elif next%3 == 0 and next % 5 != 0:
    print("Fizz")

else:
    print(next)
