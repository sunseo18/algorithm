def solution(players, callings):

    rank_dict = {name : rank for rank,name in enumerate(players) }
    for c in callings:
        # c의 현재 index
        player_idx = rank_dict[c]
        
        # players 배열에 반영
        faster_before = players[player_idx - 1]
        players[player_idx - 1] = c
        players[player_idx] = faster_before
        
        # c의 현재 index -= 1
        rank_dict[c] -= 1
        # faster_before의 현재 index += 1
        rank_dict[faster_before] += 1
        
    answer = [ x[0] for x in sorted( rank_dict.items() , key = lambda x : x[1])]
    
        
    return answer