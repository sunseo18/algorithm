from collections import Counter

def solution(k, tangerine):
        

    count_list = sorted(list(Counter(tangerine).values()), reverse = True)
    

    answer, t = 0, 0
    for no in count_list:
        t += no
        answer += 1
        if t >= k:
            break
        
    return answer