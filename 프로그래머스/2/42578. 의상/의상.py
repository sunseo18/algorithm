from collections import defaultdict
def solution(clothes):
    clothes_dict = defaultdict(list)
    
    for cloth in clothes:
        clothes_dict[cloth[1]].append(clothes_dict)
        
    keys = clothes_dict.keys()
    
    answer = 1
    
    for key in keys:
        answer *= len(clothes_dict[key]) + 1
    
    return answer-1