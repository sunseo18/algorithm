from collections import defaultdict
def solution(weights):
    answer = 0
    weights.sort()
    dic = defaultdict(int)
    
    for weight in weights:
        two_of_three = weight * 2 / 3
        two_of_four = weight * 2 / 4
        three_of_four = weight * 3 / 4
        
        if weight in dic:
            answer += dic[weight]
        if two_of_three in dic:
            answer += dic[two_of_three]
        if two_of_four in dic:
            answer += dic[two_of_four]
        if three_of_four in dic:
            answer += dic[three_of_four]
        dic[weight] += 1
            
    return answer