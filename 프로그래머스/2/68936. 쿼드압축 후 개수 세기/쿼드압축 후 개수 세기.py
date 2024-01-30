def solution(arr):
    answer = [0, 0]
    def recurse(arr):
        length = len(arr)
        no_1 = 0
        no_0 = 0
        for row in arr:
            for col in row:
                if col == 1:
                    no_1 = 1
                elif col == 0:
                    no_0 = 1

        if no_1 == 1 and no_0 == 0:
            answer[1] += 1
            return
        if no_1 == 0 and no_0 == 1:
            answer[0] += 1
            return
        else:
            index = (length+1)//2
            recurse([a[:index]for a in arr][:index])
            recurse([a[:index]for a in arr][index:])
            recurse([a[index:] for a in arr][:index])
            recurse([a[index:] for a in arr][index:])
            
    recurse(arr)
    return answer