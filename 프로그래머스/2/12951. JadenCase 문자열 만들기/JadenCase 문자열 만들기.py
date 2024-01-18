def solution(s):
    length = len(s)
    
    answer = ''
    if s[0].isnumeric():
        answer += s[0]
    else:
        answer += s[0].upper()
        
    for i in range(1, length):
        # 빈 칸이면 그대로 복사
        if s[i] == ' ':
            answer += ' '
            continue
            
        # 첫 번째 단어면 
        if s[i-1] == ' ':
            # 숫자면 그대로
            if s[i].isnumeric():
                answer += s[i]
            # 알파벳이면 대문자로
            else:
                answer += s[i].upper()
        
        
        # 그 외 단어면 lower
        else:
            answer += s[i].lower()
            
    return answer
                