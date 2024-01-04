def solution(polynomial):    
    
    p_list = polynomial.split('+')
    x_total = 0
    const_total = 0
    for p in p_list:
        p = p.strip()
        if 'x' in p:
            p = p[:-1]
            if not p:
                x_total+=1
            else:
                x_total+=int(p)
        else:
            const_total+=int(p)    
    
    answer = ""
    if x_total != 0 and x_total != 1:
        answer += f"{x_total}x"

    if x_total == 1:
        answer += "x"
    if x_total != 0 and const_total != 0:
        return answer + f" + {str(const_total)}"
    if x_total == 0 and const_total != 0:
        return str(const_total)
    return answer