def check_common_multiple(arr, common_multiple):
    for no in arr:
        if common_multiple % no != 0:
            return False
    return True

def solution(arr):
    answer = 0
    
    max_no = max(arr)
    max_answer = 1
    for a in arr:
        max_answer *= a
    
    for n in range(max_no, max_answer+1):
        if check_common_multiple(arr, n) == False:
            continue
        else:
            return n
    
