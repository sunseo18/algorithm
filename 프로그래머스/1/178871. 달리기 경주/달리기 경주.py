def solution(players, callings):

    rank_dict = {name : rank for rank,name in enumerate(players) }
    for c in callings:
        # c의 현재 index
        player_idx = rank_dict[c]
        
        # c의 현재 index -= 1
        rank_dict[c] -= 1
        # faster_before의 현재 index += 1
        rank_dict[players[player_idx - 1]] += 1  
        
        # players 배열에 반영
        players[player_idx-1], players[player_idx] = players[player_idx], players[player_idx-1]
        

        

        
    return players