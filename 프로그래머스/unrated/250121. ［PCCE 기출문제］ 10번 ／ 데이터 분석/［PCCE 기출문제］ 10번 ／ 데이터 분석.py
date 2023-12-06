def solution(data, ext, val_ext, sort_by):
    ext_dict = {"code": 0, "date": 1, "maximum": 2, "remain": 3}
    
    semi_answer = []

    # val_ext보다 더 작은 값들 검색
    semi_answer = [ d for d in data if d[ext_dict[ext]] < val_ext ]

    # 정렬
    semi_answer.sort( key = lambda k : k[ext_dict[sort_by]])

    return semi_answer