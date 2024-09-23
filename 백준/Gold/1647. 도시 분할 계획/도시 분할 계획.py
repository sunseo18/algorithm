import sys

n, m = map(int, sys.stdin.readline().split())

vertex= []
for i in range(m):
    a, b, length = map(int, sys.stdin.readline().split())

    vertex.append((length, a, b))

vertex.sort()


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
    elif parent_a > parent_b:
        parent_list[parent_a] = parent_b


parent_list = [i for i in range(n+1)]

answer = 0
last = 0
for length, a, b in vertex:
    if find_parent(parent_list, a) != find_parent(parent_list, b):
        union(parent_list, a, b)
        answer += length
        last = length

print(answer-last)
