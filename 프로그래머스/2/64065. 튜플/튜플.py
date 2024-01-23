from collections import defaultdict
def solution(s):
    sets = s[2:-2]
    
    sets = sets.split("},{")
    
    length = len(sets)
    for i in range(length):
        sets[i] = set(sets[i].split(","))
        
    dic = defaultdict(int)
    
    for s in sets:
        dic[len(s)] = s
    
    answer = [int(list(dic[1])[0])]
    for i in range(2, length+1):
        answer.append(int(list(dic[i] - dic[i-1])[0]))
        
    
    return answer