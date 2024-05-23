import sys

n, k = map(int, sys.stdin.readline().strip().split())

array = list(map(int, sys.stdin.readline().strip().split()))


if n == k:
    sys.stdout.write(str(sum(array)))
    sys.exit()

end_index = k-1
    
tmp = sum(array[0:k])
answer = tmp

for i in range(1, n):
    tmp += array[(end_index+1) % n]
    tmp -= array[i-1]

    end_index  = (end_index+1)%n 
    if tmp > answer:
        answer = tmp
    

sys.stdout.write(str(answer))
