def add_10_min(time):
    hour, min = time.split(":")

    after_10_min = int(min) + 10
    after_10_min_str = str(after_10_min)
    
    if after_10_min >= 60:
        after_10_min -= 60
        if len(str(after_10_min)) == 1:
            after_10_min_str = "0" + str(after_10_min)
        hour = str(int(hour) + 1)
        if len(hour) == 1:
            hour = "0" + hour
    return hour + ":" + after_10_min_str
    
def is_book_time_colapsed(book_a_end, book_b_start):
    if book_a_end <= book_b_start:
            return False
    return True
    
def solution(book_time):
    end_time = []
    book_time.sort()
    for b in book_time:
        b[1] = add_10_min(b[1])
    
    # print(book_time)
    
    end_time = [book_time[0][1]]
    for b in book_time[1:]:
        collapsed = True
        for i in range(len(end_time)):
            # 하나라도 안 겹치는 거 있는지 검사
            if not is_book_time_colapsed(end_time[i], b[0]):
                collapsed = False
                break
        if not collapsed:
            # print("충돌 안 함")
            end_time[i] = b[1]
        else:
            end_time.append(b[1])

    return len(end_time)