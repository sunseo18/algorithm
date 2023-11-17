def solution(s, skip, index):
    answer = []
    alphabet = 'abcdefghijklmnopqrstuvwxyz' * 3

    for ch in s:
        ch_idx = alphabet.index(ch)
        
        skip_no = 0
        for a in alphabet[ch_idx+1:]:
            if a not in skip:
                skip_no += 1
            if skip_no == index:
                answer.append(a)
                break

    return "".join(answer)