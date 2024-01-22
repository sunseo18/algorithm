def solution(x, y, n):
    
    val_set = set()
    queue = [x]
    no = 0

    
    while queue:
        tmp = []
        while queue:
            q = queue.pop()
            if q == y:
                return no

            if q < y:
                plus = q+n
                if plus not in val_set:
                    tmp.append(plus)
                    val_set.add(plus)
                
                time_2 = q * 2
                if time_2 not in val_set:
                    tmp.append(time_2)
                    val_set.add(time_2)
                    
                time_3 = q * 3
                if time_3 not in val_set:
                    tmp.append(time_3)
                    val_set.add(time_3)

        no += 1
        queue = tmp
    
    return -1
