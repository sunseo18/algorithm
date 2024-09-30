import sys

input = sys.stdin.readline

n, m = map(int, input().split())


parent_list = [i for i in range(n)]


def find_parent(parent_list, i):
    if parent_list[i] == i:
        return i

    parent_list[i] = find_parent(parent_list, parent_list[i])
    return parent_list[i]

def union(parent_list, a, b):
    parent_a = find_parent(parent_list, a)
    parent_b = find_parent(parent_list, b)


    if parent_a < parent_b:
        parent_list[parent_b] = parent_a
    elif parent_a > parent_b:
        parent_list[parent_a] = parent_b

for i in range(m):
    s, e = map(int, input().split())

    if find_parent(parent_list, s) == find_parent(parent_list, e):
        print(i+1)
        sys.exit()

    union(parent_list, s, e)

print(0)


    
