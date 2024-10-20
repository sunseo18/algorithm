import sys

input = sys.stdin.readline

sys.setrecursionlimit(10**9)

n = int(input())
broken_numbers_length = int(input())

numbers = [str(i) for i in range(0, 10)]

if broken_numbers_length != 0:
    broken_numbers = list(input().split())

    for i in range(broken_numbers_length):
        numbers.remove(broken_numbers[i])


if n == 100:
    print(0)
    sys.exit()


_min = abs(n - 100)

def dfs(tmp, numbers, depth):
    global _min


    
    if depth == -1:
        return


    for i in range(len(numbers)):
        tmp[depth] = numbers[i]
        
        tmp_number = int("".join(tmp))
        tmp_min = len(str(tmp_number)) + abs(tmp_number - n)

        if tmp_min < _min:
            _min = tmp_min
            
        dfs(tmp, numbers, depth-1)
        tmp[depth] = '0'


dfs(['0' for _ in range(6)], numbers, 5)

print(_min)

