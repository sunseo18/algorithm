bracket_dict = {"]": "[", "}": "{", ")": "(", "(": "-", "[": "-", "{": "-"}

def check_right(s):
    stack = []
    for bracket in s:
        if stack:
            if bracket_dict[bracket] == stack[-1]:
                stack.pop()
            else:
                stack.append(bracket)
        else:
            stack.append(bracket)

    if stack:
        return False
    return True

def solution(s):
    
    answer = 0
    for i in range(len(s)):
        if check_right(s):
            answer += 1
        first = s[0]
        s= s[1:] + first
        
    return answer