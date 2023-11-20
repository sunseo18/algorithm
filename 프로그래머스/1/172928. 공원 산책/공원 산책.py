def check_obstacle(park, direction_dict, start, direction, amount):
    for i in range(amount):
        if park[start[0] + direction_dict[direction][0]*(i+1)][start[1] + direction_dict[direction][1]*(i+1)] == "X":
            return True
    return False
    
    
    
def solution(park, routes):
    max_width = len(park[0]) - 1
    max_height = len(park) - 1
    
    direction_dict = {"E": [0, 1], "S": [1, 0], "N": [-1, 0], "W": [0, -1]}
    start = [0] * 2
    # 시작 지점 찾기
    for i in range(len(park)):
        for j in range(len(park[i])):
            for c in park[i][j]:
                if c == "S":
                    start[0] = i
                    start[1] = j

    for route in routes:
        direction = route[0]
        amount = int(route[2])
        
        moved_y = start[0] + direction_dict[direction][0]*amount
        moved_x = start[1] + direction_dict[direction][1]*amount
        if moved_y < 0 or moved_y > max_height:
            continue
        if moved_x < 0 or moved_x > max_width:
            continue
        if check_obstacle(park, direction_dict, start, direction, amount):
            continue

        
        start[0] = moved_y
        start[1] = moved_x
    return start