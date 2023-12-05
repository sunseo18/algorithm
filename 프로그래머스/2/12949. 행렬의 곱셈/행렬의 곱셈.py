def solution(arr1, arr2):
    answer = []
    arr1_i = len(arr1)
    arr1_j = len(arr1[0])
    
    arr2_i = len(arr2)
    arr2_j = len(arr2[0])
    
    for j in range(arr1_i):
        semi = []
        for k in range(arr2_j):
            add = 0
            for i in range(arr1_j):
                add += arr1[j][i] * arr2[i][k]
            semi.append(add)
        answer.append(semi)

    return answer