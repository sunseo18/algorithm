import sys


n, m = map(int, sys.stdin.readline().split())

min_couple = 10001

min_one = 10001

for _ in range(m):
    couple, one = map(int, sys.stdin.readline().split())

    min_couple = min(min_couple, couple)
    min_one = min(min_one, one)



calc_couple = n//6 * min_couple
calc_one = n%6 * one

if calc_one > min_couple:
    calc_one = min_couple
    
print(min(calc_couple+calc_one, min_one*n))

