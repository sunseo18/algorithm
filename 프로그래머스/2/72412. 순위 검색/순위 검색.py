def binary_search(arr, start, end, target):
    while start < end:
        mid = start + (end - start) // 2
        if arr[mid] >= target:
            end = mid
        else:
            start = mid + 1
    return start
            
        
def solution(info, query):
    answer = []
    dictionary = dict()
    for code in ["cpp", "java", "python", "-"]:
        for work in ["backend", "frontend", "-"]:
            for year in ["junior", "senior", "-"]:
                for food in ["chicken", "pizza", "-"]:
                    key = f"{code} {work} {year} {food}"
                    dictionary[key] = []
                    
    for i in info:
        splitted_i = i.split()
        for code in [splitted_i[0], "-"]:
            for work in [splitted_i[1], "-"]:
                for year in [splitted_i[2], "-"]:
                    for food in [splitted_i[3], "-"]:
                        dictionary[f"{code} {work} {year} {food}"].append(int(splitted_i[-1]))
                        
    for d in dictionary:
        dictionary[d].sort()

    for q in query:
        splitted_q = q.replace("and ", "").split()
        key = f"{splitted_q[0]} {splitted_q[1]} {splitted_q[2]} {splitted_q[3]}"
        target_score = int(splitted_q[-1])
        scores = dictionary[key]
        answer.append(len(scores) - binary_search(dictionary[key], 0, len(scores), target_score))
        
    return answer