import sys

def recursion(s, l, r):
    global count
    count += 1
    if l >= r:
        return 1
    if s[l] != s[r]:
        return 0
    else:
        return recursion(s, l+1, r-1)


def isPalindrome(s):
    return recursion(s, 0, len(s) -1)

n = int(input())

for _ in range(n):
    count = 0
    print(isPalindrome(sys.stdin.readline().strip()), count)
