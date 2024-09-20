import sys

sys.setrecursionlimit(10**6)

t = int(sys.stdin.readline())

def find_parent(parent_dict, person):
    if parent_dict[person] == person:
        return person

    parent_dict[person] = find_parent(parent_dict, parent_dict[person])
    return parent_dict[person]

def union(parent_dict, count_dict, a, b):
    parent_a = find_parent(parent_dict, a)
    parent_b = find_parent(parent_dict, b)


    if parent_a != parent_b:
        parent_dict[parent_b] = parent_a
        count_dict[parent_a] += count_dict[parent_b]

for _ in range(t):
    n = int(sys.stdin.readline())

    parent_dict = dict()
    count_dict = dict()
    
    for _ in range(n):
        first, second = sys.stdin.readline().split()

        if first not in parent_dict:
            parent_dict[first] = first
            count_dict[first] = 1

        if second not in parent_dict:
            parent_dict[second] = second
            count_dict[second] = 1

        union(parent_dict, count_dict, first, second)

        root = find_parent(parent_dict, first)
        print(count_dict[root])
        
        
        
