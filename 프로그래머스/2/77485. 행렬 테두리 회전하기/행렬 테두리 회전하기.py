def solution(rows, columns, queries):
    answer = []
    no = [ [0 for i in range(columns)] for i in range(rows)]

    for i in range(rows):
        for j in range(columns):
            no[i][j] = ((i) * columns +j +1)
            
    for query in queries:
        index_list = []
        left = [query[0]-1, query[1]-1]
        right = [query[2]-1, query[3]-1]
        
        # 위 가로
        for i in range(left[1], right[1]+1):
            index_list.append([left[0], i])
            
        # 오른쪽 세로
        for i in range(left[0]+1, right[0]+1):
            index_list.append([i, right[1]])
        
        # 아래 가로
        for i in range(right[1]-1, left[1]-1, -1):
            index_list.append([right[0], i])
            
        # 왼쪽 세로
        for i in range(right[0]-1, left[0]-1, -1):
            index_list.append([i, left[1]])
                
        before = no[index_list[0][0]][index_list[0][1]]
        min_no = before
        # 값 옮기기
        for i in range(1, len(index_list)):
            tmp = no[index_list[i][0]][index_list[i][1]]
            no[index_list[i][0]][index_list[i][1]] = before
            before = tmp
            # 최솟값 구하기
            if tmp < min_no:
                min_no = tmp
                
        answer.append(min_no)

        
    return answer