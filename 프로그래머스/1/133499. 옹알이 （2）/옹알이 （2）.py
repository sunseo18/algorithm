def is_continuous_word(word):
    for i in range(len(word)-1):
        if word[i] == word[i+1]:
            return True
    return False

def solution(babbling):
    answer = 0
    can = ["aya", "ye", "woo", "ma"]
    
    for i in range(len(babbling)):
        babbling[i] = babbling[i].replace("aya", "0")
        babbling[i] = babbling[i].replace("ye", "1")
        babbling[i] = babbling[i].replace("woo", "2")
        babbling[i] = babbling[i].replace("ma", "3")
        

    for b in babbling:
        if not b.isnumeric():
            continue
        else:
            if not is_continuous_word(b):
                answer += 1  
                
            
    # for i in range(len(babbling)):
    #     for j in range(len(babbling[i])):
    #         if not babbling[i][j].isnumeric():
    #             continue
    #         if j != 0:
    #             if babbling[i][j-1] == babbling[i][j]:
    #                 continue
    #         answer += 1

        
    return answer