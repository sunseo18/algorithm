def solution(s):
    s_list = list(s)
    no = 0
    count_0 = 0
    while s != '1':
        no += 1
        count_1 = 0
        for c in s:
            if c == '0':
                count_0 += 1
            else:
                count_1 += 1

        s = str(bin(count_1)[2:])

    return [no, count_0]