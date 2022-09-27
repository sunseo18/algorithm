def solution(numbers):
    length = len(numbers)
    if length == 1:
        return numbers
    
    answer = []
    for n in range(length-1):
        for i in range(n+1, length):
            answer.append(numbers[n]+numbers[i])
            
    return sorted(list(set(answer)))
