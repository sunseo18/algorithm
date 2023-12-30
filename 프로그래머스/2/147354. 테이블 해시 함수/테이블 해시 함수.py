def solution(data, col, row_begin, row_end):
    
    tmp_dict = dict()
    total_list = list()
    before_hash = []
    
    for row in data:
        if row[col-1] in tmp_dict.keys():
            tmp_dict[row[col-1]].append(row)
        else:
            tmp_dict[row[col-1]] = [row]
        
    for k in tmp_dict.keys():
        total_list += sorted(tmp_dict[k], reverse = True)
        
    total_list.sort(key = lambda x: x[col-1])

        
    for i in range(row_begin-1, row_end):
        tmp = 0
        for t in total_list[i]:
            tmp += t % (i+1)
        before_hash.append(tmp)
    
    result = before_hash[0]
    for i in range(1, len(before_hash)):
        result = result ^ before_hash[i]
        
    return result