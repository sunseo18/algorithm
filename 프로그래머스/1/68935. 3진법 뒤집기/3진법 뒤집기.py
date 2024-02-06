def solution(n):
    three_straight = ''
    
    while n > 0:
        three_straight = str(n%3) + three_straight
        n //= 3

    length = len(three_straight)
    print(three_straight)
    
    answer = 0
    for i in range(length):
        answer += int(three_straight[i]) * (3**i)
    
    
    return answer