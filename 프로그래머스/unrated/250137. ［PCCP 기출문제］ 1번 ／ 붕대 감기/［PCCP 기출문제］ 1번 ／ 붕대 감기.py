def solution(bandage, health, attacks):
    answer = health
    health_list_length = attacks[-1][0] + 1
    health_list = [0] * health_list_length
    sequencial_bandage = 0
    
    for attack in attacks:
        health_list[attack[0]] = attack[1] * -1
    
    for i in range(1, health_list_length):
        if health_list[i] < 0:
            sequencial_bandage = 0
        else:
            health_list[i] = bandage[1]
            sequencial_bandage += 1
            
            if sequencial_bandage == bandage[0]:
                health_list[i] += bandage[2]
                sequencial_bandage = 0
    
    for i in range(1, health_list_length):
        if answer + health_list[i] > health:
            answer = health
        elif answer + health_list[i] <=  0:
            return -1
        else:
            answer += health_list[i]

            

    return answer