import sys

n = int(sys.stdin.readline().strip())

array = [0, 3, 7]

for i in range(3, n+1):
    array.append((2*array[i-1] + array[i-2]) % 9901)
    

print(array[n])
