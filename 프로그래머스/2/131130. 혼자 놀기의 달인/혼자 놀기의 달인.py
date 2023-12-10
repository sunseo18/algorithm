def group_no(i, opened, cards):
    no = 0
    while not opened[i]:
        opened[i] = True
        no += 1
        next_idx = cards[i] -1
        i = next_idx
        
    return no
    
    
def solution(cards):
    no = []
    length = len(cards)
    opened = [False] * length
    
    for i in range(length):
        if not opened[i]:
            no.append(group_no(i, opened, cards))
            
    no.sort(reverse = True)
    
    if len(no) == 1:
        return 0
    
    return no[0] * no[1]