import sys

n, k = map(int, sys.stdin.readline().strip().split())


array = [i for i in range(1, n+1)]

length = n
index = k-1

sys.stdout.write('<')
while array:
    sys.stdout.write(str(array.pop(index)))
    length -= 1

    if length == 0:
        break
    index = (index + k - 1) % length
    sys.stdout.write(', ')
sys.stdout.write('>')
