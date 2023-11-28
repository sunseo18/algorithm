def solution(n, words):
    차례 = [0] * (n+1)
    차례[1] += 1
    
    for i in range(1, len(words)):
        말하는사람 = n if (1+i)%n == 0 else (1+i)%n
        차례[말하는사람] += 1
        
        if words[i] in words[:i]:
            return [말하는사람, 차례[말하는사람]]
        if words[i-1][-1] != words[i][0]:
            return [말하는사람, 차례[말하는사람]]
        
    return [0, 0]
