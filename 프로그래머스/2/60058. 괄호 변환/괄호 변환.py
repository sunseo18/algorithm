def correct_brackets(brackets):
    count = 0
    for b in brackets:
        if b == "(":
            count += 1
        else:
            count -=1
        if count < 0:
            return False
                
    return True
        
def switch(brackets):
    result = ""
    for i in range(len(brackets)):
        if brackets[i] == ")":
            result += "("
        else:
            result += ")"
    return result

def balanced_to_right(brackets):
    bracket_len = len(brackets)
    if not brackets:
        return ""
    
    right_num, left_num = 0, 0
    for i in range(bracket_len): 
        if brackets[i] == ")":
            right_num += 1
        elif brackets[i] == "(":
            left_num += 1
        # 균형잡힌 괄호 문자열이면
        if right_num == left_num:
            u = brackets[:i+1]
            v = brackets[i+1:]
            # 올바른 문자열이 아니면
            if not correct_brackets(u):
                result1 = '('
                result1 += balanced_to_right(v)
                result1 += ')'
                u = u[1:len(u)-1]
                result1 += switch(u)
                return result1
            # 올바른 문자열이면:
            else:
                # 나머지 문자열에 대해서 다시 수행
                result2 = balanced_to_right(v)
                result2 = u + result2
                return result2
            
def solution(p):
    answer = balanced_to_right(p)

    return ''.join(answer)