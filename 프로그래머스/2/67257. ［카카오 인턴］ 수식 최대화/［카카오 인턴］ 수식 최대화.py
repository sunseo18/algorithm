def calculate(number_list, operand_list, priority):
    operand_list_length = len(operand_list)
    no_copy = number_list.copy()
    op_copy = operand_list.copy()
    for p in priority:
        i = 0
        while i < operand_list_length:
            if op_copy[i] == p:
                n1 = no_copy.pop(i)
                n2 = no_copy.pop(i)
                no_copy.insert(i, str(eval(n1 + p + n2)))
                op_copy.pop(i)
                if i != 0:
                    i -=1
                operand_list_length -= 1
            else:
                i+=1

                
    return abs(int(no_copy[0]))
                
def solution(expression):
    possible_operands = ['-', '+', '*']
    
    numbers = expression.replace("-", " ").replace("*", " ").replace("+", " ")
    number_list = numbers.split(" ")
        
    operand_list = []
    for e in expression:
        if not e.isnumeric():
            operand_list.append(e)
    
    
    used_operand_list = list(set(operand_list))
    print(number_list)
    print(used_operand_list)
    
    if len(used_operand_list) == 1:
        return abs(eval(expression))
    if len(used_operand_list) == 2:
        return max(calculate(number_list, operand_list, [used_operand_list[0], used_operand_list[1]]), calculate(number_list, operand_list, [used_operand_list[1], used_operand_list[0]]))
                   
    if len(used_operand_list) == 3:
        return max(calculate(number_list, operand_list, [used_operand_list[0], used_operand_list[1], used_operand_list[2]]), calculate(number_list, operand_list, [used_operand_list[0], used_operand_list[2], used_operand_list[1]]), calculate(number_list, operand_list, [used_operand_list[1], used_operand_list[0], used_operand_list[2]]), calculate(number_list, operand_list, [used_operand_list[1], used_operand_list[2], used_operand_list[0]]), calculate(number_list, operand_list, [used_operand_list[2], used_operand_list[0], used_operand_list[1]]), calculate(number_list, operand_list, [used_operand_list[2], used_operand_list[1], used_operand_list[0]]))
    answer = 0
    return answer