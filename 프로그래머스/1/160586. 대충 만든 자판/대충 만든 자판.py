def get_target_word_answer(key_dict, target):
    answer = 0
    for t in target:
        if t in key_dict:
            answer += key_dict[t]
        else:
            return -1
    return answer
        
def solution(keymap, targets):
    key_dict = dict()
    for key in keymap:
        for i in range(len(key)):
            if key[i] in key_dict:
                if key_dict[key[i]] > i+1:
                    key_dict[key[i]] = i+1
            else:
                key_dict[key[i]] = i+1
                
    targets_len = len(targets)
    answer = [ 0 ] * targets_len 

    for i in range(targets_len):
        answer[i] = get_target_word_answer(key_dict, targets[i])

        
    return answer