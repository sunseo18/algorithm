from collections import Counter

def count_characters(no):
    char_count = Counter(no)

    
    return char_count 

def solution(X, Y):      
    char_count = count_characters(Y)
    
    same_no = []
    for x in X:
        if char_count[x] != 0:
            char_count[x] -= 1
            same_no.append(x)
    
    if len(same_no) == 0:
        return "-1"

    same_no.sort(reverse = True)
    
    to_str = "".join(same_no)
    
    for s in to_str:
        if s != "0":
            return to_str
        
    return "0"
