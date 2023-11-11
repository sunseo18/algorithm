def check_rank(no):
    if no == 6: 
        return 1
    elif no == 5:
        return 2
    elif no == 4:
        return 3
    elif no == 3:
        return 4
    elif no == 2:
        return 5
    else:
        return 6

def solution(lottos, win_nums):
    min_num = 0
    max_num = 0
    for l in lottos:
        if l in win_nums:
            max_num += 1
            min_num += 1
        if l == 0:
            max_num += 1
        
    return [check_rank(max_num), check_rank(min_num)]