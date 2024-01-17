def solution(s):
    int_str_array = s.split()
    
    int_array = []
    
    for no in int_str_array:
        int_array.append(int(no))
        
    int_array.sort()
    
    return f'{int_array[0]} {int_array[-1]}'