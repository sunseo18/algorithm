def get_collapse(target_a, target_b):
    collapse_0 = max(target_a[0], target_b[0]+1)
    collapse_1 = min(target_a[1], target_b[1])
    
    if collapse_0 > collapse_1:
        return None
    
    return [collapse_0, collapse_1]

def solution(targets):
    # 일단 정렬
    targets.sort()
    targets_len = len(targets)
    
    collapse = None
    answer = 1
    # 겹치는 것 하나로 묶어서 격추
    for i in range(1, targets_len):
        # 이전 겹침 비어있을 때 (새 시작)
        if not collapse:
            # 새로운 겹침 계산
            new_collapse = get_collapse(targets[i-1], targets[i])
            # 겹침 없음
            if not new_collapse:
                answer += 1
            # 겹침 있음
            else:
                collapse = new_collapse
        
        # 이전 겹침 있을 때
        if collapse:
            # 현재 값과 이전 겹침 비교
            new_collapse = get_collapse(collapse, targets[i])
            if not new_collapse:
                answer += 1
                collapse = None
            else:
                collapse = new_collapse
                            
            
    return answer