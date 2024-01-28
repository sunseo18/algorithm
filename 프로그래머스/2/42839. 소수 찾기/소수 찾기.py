from itertools import permutations

def check_sosu(number):
    if number == 1 or number == 0:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

def solution(numbers):
    sosu_dict = dict()
    answer = 0
    no_list = list(numbers)
    length = len(no_list)

    for l in range(1, length+1):
        tmp_no_list = set(permutations(no_list, l))
    
        for no_tuple in tmp_no_list:
            number = int("".join(no_tuple))
            
            if number in sosu_dict:
                continue
                
            if check_sosu(number):
                answer += 1
                sosu_dict[number] = True
                
    
    return answer