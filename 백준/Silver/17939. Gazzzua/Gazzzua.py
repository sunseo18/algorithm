import sys

input = sys.stdin.readline
N = int(input())

li = (list(map(int,input().split())))
li.reverse()
max_li = li[0] 
result = 0  

for i in li:
    if i> max_li: 
        max_li = i
    else:
        result += (max_li) - i
print(result)