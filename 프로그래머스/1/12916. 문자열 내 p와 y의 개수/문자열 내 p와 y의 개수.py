def check_if_p_and_y_num_is_same(string):
    p_num = 0
    y_num = 0
    for s in string:
        if s == 'p' or s == 'P':
            p_num += 1
        if s == 'y' or s == 'Y':
            y_num += 1
    
    return p_num == y_num
    
        
def solution(s):
    return check_if_p_and_y_num_is_same(s)
    