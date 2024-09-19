import sys

def find_parent(parent_list, a):
    if parent_list[a] == a:
        return a

    parent_list[a] = find_parent(parent_list, parent_list[a])
    return parent_list[a]


def union(parent_list, a, b):
    parent_a = find_parent(parent_list, a)
    parent_b = find_parent(parent_list, b)

    if parent_a < parent_b:
        parent_list[parent_b] = parent_a

    else:
        parent_list[parent_a] = parent_b
        
input = sys.stdin.readline

n = int(input())
m = int(input())

maps = [[] for _ in range(n)]
parent_list = [i for i in range(n)]

for i in range(n):
    maps[i] = list(map(int, input().split()))

for i in range(n):
    for j in range(n):
        if maps[i][j] == 1:
            union(parent_list, i, j)

visits = list(map(int, input().split()))

if not visits:
    print("YES")
    sys.exit()

parent = find_parent(parent_list, visits[0]-1)

for v in visits:
    if find_parent(parent_list, v-1) != parent:
        print("NO")
        sys.exit()
print("YES")
sys.exit()

    
