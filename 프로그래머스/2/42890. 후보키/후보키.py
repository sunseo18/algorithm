from itertools import combinations
from collections import Counter

def get_rels(comb, comb_len, relation):
    if comb_len == 1:
        return [rel[comb[0]] for rel in relation]
    elif comb_len == 2:
        return [ (rel[comb[0]], rel[comb[1]]) for rel in relation ]
    elif comb_len == 3:
        return [ (rel[comb[0]], rel[comb[1]], rel[comb[2]]) for rel in relation ]
    elif comb_len == 4:
        return [ (rel[comb[0]], rel[comb[1]], rel[comb[2]], rel[comb[3]]) for rel in relation ]
    elif comb_len == 5:
        return [ (rel[comb[0]], rel[comb[1]], rel[comb[2]], rel[comb[3]], rel[comb[4]]) for rel in relation ]
    elif comb_len == 6:
        return [ (rel[comb[0]], rel[comb[1]], rel[comb[2]], rel[comb[3]], rel[comb[4]], rel[comb[5]]) for rel in relation ]
    elif comb_len == 7:
        return [ (rel[comb[0]], rel[comb[1]], rel[comb[2]], rel[comb[3]], rel[comb[4]], rel[comb[5]], rel[comb[6]]) for rel in relation ]
    elif comb_len == 8:
        return [ (rel[comb[0]], rel[comb[1]], rel[comb[2]], rel[comb[3]], rel[comb[4]], rel[comb[5]], rel[comb[6]], rel[comb[7]]) for rel in relation ]

def element_contain(keys, comb):
    for key in keys:
        result = True
        for k in key:
            if k not in comb:
                result = False
        if result:
            return True
    return False
    
def solution(relation):
    col = len(relation[0])
    key = []
    col_index = [i for i in range(col)]
    
    for i in range(1, col+1):
        combs = combinations(col_index, i)
        
        for comb in combs:
            if element_contain(key, comb):
                continue
                
            tmp = get_rels(comb, i, relation)       
            count_val= Counter(tmp).values()
            
            all_1 = True
            for v in count_val:
                if v != 1:
                    all_1 = False
            
            if all_1:
                key.append(comb)
    
    print(key)
    return len(key)