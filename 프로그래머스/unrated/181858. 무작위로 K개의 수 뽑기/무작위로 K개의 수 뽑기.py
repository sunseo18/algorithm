def solution(arr, k):
    new_arr = [arr[0]]
    i = 1
    for a in arr[1:]:
        if a in new_arr:
            continue
        new_arr.append(a)
        i+=1
        if i == k:
            break
    
    if len(new_arr) < k:
        for _ in range(k - len(new_arr)):
            new_arr.append(-1)
            
    return new_arr