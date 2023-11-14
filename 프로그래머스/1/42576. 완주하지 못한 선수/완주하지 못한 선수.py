def solution(participant, completion): 
    answer = ""
    participant.sort()
    completion.sort()
    
    participant_len = len(participant)
    for i in range(participant_len):
        if i == participant_len-1:
            return participant[-1]
        if participant[i] != completion[i]:
            return participant[i]

    return participant[0]