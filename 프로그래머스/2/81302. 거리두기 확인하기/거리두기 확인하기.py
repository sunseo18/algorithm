direction = {"right": [0, 1], "left": [0, -1], "up": [-1, 0], "down": [1, 0]}
direction_two = {"left_up": [-1, -1], "right_up": [-1, 1], "left_down": [1, -1], "right_down": [1, 1]}
# 거리두기 안됐으면 False, 됐으면 True 리턴
def okay(place):
    for i in range(5):
        for j in range(5):
            if place[i][j] == 'P': 
                for key in direction.keys():
                    moved_i = i+direction[key][0]
                    moved_j = j+direction[key][1]
                    if moved_i >= 0 and moved_j >= 0 and moved_i < 5 and moved_j < 5:
                        moved = place[moved_i][moved_j]
                        if moved == 'P':
                            return False
                        elif moved == 'O':
                            twice_moved_i = i+(direction[key][0] * 2)
                            twice_moved_j = j+(direction[key][1] * 2)
                            if twice_moved_i >= 0 and twice_moved_j >= 0 and twice_moved_i < 5 and twice_moved_j < 5:
                                if place[twice_moved_i][twice_moved_j] == 'P':
                                    return False
                for key in direction_two.keys():
                    moved_i = i+direction_two[key][0]
                    moved_j = j+direction_two[key][1]
                    if moved_i >= 0 and moved_j >= 0 and moved_i < 5 and moved_j < 5:
                        moved = place[moved_i][moved_j]
                        # print("moved: ", moved_i, moved_j, moved)
                        if moved == 'P':
                            if place[i][moved_j] == 'O' or place[moved_i][j] == 'O':
                                return False
    return True
            
def solution(places):
    answer = []
    for place in places:
        if okay(place):
            answer.append(1)
        else:
            answer.append(0)
            
    return answer