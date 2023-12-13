def correct_brackets(brackets):
    if not brackets:
        return True
    
    stack = []
    
    for b in brackets:
        if not stack:
            stack.append(b)
            
        else:
            if b == ")" and stack[-1] == "(":
                stack.pop()
                
            else:
                stack.append(b)
                
                
    if not stack:
        return True
    return False
        
def switch(brackets):
    for i in range(len(brackets)):
        if brackets[i] == ")":
            brackets[i] = "("
        else:
            brackets[i] = ")"
    return brackets

# answer = []
def balanced_to_right(brackets):
    # global answer
    bracket_len = len(brackets)
    if not brackets:
        return []
    
    right_num, left_num = 0, 0
    for i in range(bracket_len):
        # bracket 비교 
        if brackets[i] == ")":
            right_num += 1
        elif brackets[i] == "(":
            left_num += 1
        # 균형잡힌 괄호 문자열
        if right_num == left_num:
            u = brackets[:i+1]
            v = brackets[i+1:]
            print(u,v)
            # 올바른 문자열이 아니면
            if not correct_brackets(u):
                print("zz")
                result1 = ['(']
                result1 += balanced_to_right(v)
                result1.append(')')
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
    p = list(p)
    answer = balanced_to_right(p)

    return ''.join(answer)