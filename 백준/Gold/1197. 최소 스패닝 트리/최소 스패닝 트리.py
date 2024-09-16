import sys
sys.setrecursionlimit(10**9)
infinite = float('inf')

v, e = map(int, sys.stdin.readline().split())

edges = []

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

    

for _ in range(e):
    start, end, weight = map(int, sys.stdin.readline().split())

    edges.append((weight, start, end))

edges.sort()

parent_list = [ i for i in range(v+1) ]

result = 0

for edge in edges:
    weight, start, end = edge

    # 두 노드의 부모가 다르면 두 노드 연결(union)
    if find_parent(parent_list, start) != find_parent(parent_list, end):
        union(parent_list, start, end)
        result += weight
        
print(result)

