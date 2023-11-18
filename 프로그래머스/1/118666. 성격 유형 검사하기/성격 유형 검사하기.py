def solution(survey, choices):
    answer = ''
    score_dict = { 1: 3, 2: 2, 3: 1, 4: 0, 5: 1, 6: 2, 7:3}
    personality_idx_dict = {"R": 0, "T": 1, "C": 2, "F": 3, "J": 4, "M": 5, "A": 6, "N": 7}
    idx_personlaity_dict = { v:k for k,v in personality_idx_dict.items()}
    score_list = [0] * 8
    
    for i in range(len(choices)):
        if choices[i] in [1, 2, 3]:
            score_list[personality_idx_dict[survey[i][0]]] += score_dict[choices[i]]
        else:
            score_list[personality_idx_dict[survey[i][1]]] += score_dict[choices[i]] 
    
    for i in range(0, len(score_list), 2):
        if score_list[i] > score_list[i+1]:
            answer += idx_personlaity_dict[i]
        elif score_list[i] == score_list[i+1]:
            answer += min(idx_personlaity_dict[i], idx_personlaity_dict[i+1])
        else:
            answer += idx_personlaity_dict[i+1]
            
    return answer