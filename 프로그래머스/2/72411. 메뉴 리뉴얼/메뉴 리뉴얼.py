from collections import defaultdict
from itertools import combinations

def get_same_menu(menuA, menuB):
    same_menu = ""
    length = 0
    for a in menuA:
        if a in menuB:
            length += 1
            same_menu += a
    if length > 1:
        return (same_menu, length)

def solution(orders, course):
    answer = []
    orders_list = []
    same_menu_dict = defaultdict(int)
    for order in orders:
        orders_list.append(sorted(list(order)))

    
    length = len(orders_list)
    for i in range(length-1):
        for j in range(i+1, length):
            same_menu = get_same_menu(orders_list[i], orders_list[j])
            if same_menu:
                same_menu_dict[same_menu[0]] += 1
                for c in course:
                    if c < same_menu[1]:
                        for combination in combinations(same_menu[0], c):
                            same_menu_dict["".join(combination)] += 1
                        
    for c in course:
        c_length = {k: v for k, v in same_menu_dict.items() if (len(k) == c)}
        max_order = [k for k, v in c_length.items() if v == max(c_length.values())]
        answer.extend(max_order)
    
    
    return sorted(answer)