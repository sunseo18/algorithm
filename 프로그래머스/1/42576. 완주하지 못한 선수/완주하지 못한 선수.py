from collections import Counter

def solution(participant, completion): 
    participant.sort()
    completion.sort()

    completion_len = len(completion)
    
    
    for i in range(completion_len):
        if participant[i] != completion[i]:
            return participant[i]

    return participant[-1]