import sys

hour, minute = map(int, sys.stdin.readline().strip().split())


if minute - 45 < 0:
    answer_minute = minute + 60 - 45
    answer_hour = hour - 1

    if answer_hour < 0:
        answer_hour = 23
else:
    answer_minute = minute - 45
    answer_hour = hour

print(answer_hour, answer_minute)
