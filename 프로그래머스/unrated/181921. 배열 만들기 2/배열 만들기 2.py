def solution(l, r):
    answer = []
    for x in range(l, r+1):
        x_str = str(x)
        new_x_str = x_str.replace('5', '').replace('0', '')

        if new_x_str == '':
            answer.append(x)

    if not answer:
        return [-1]
    return answer