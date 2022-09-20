def solution(board, moves):
    n = len(board)
    resultArray = []
    answer = 0

    for m in moves:
        no = findTheTop(board, m)
        if no != 0:
            answer += appendToResultArray(resultArray, no)

    return answer

def findTheTop(array, nthLine):
    length = len(array)
    for i in range(length):
        if array[i][nthLine-1] != 0:
            no = array[i][nthLine-1]
            array[i][nthLine-1] = 0
            return no
    return 0
    

def appendToResultArray(resultArray, no):
    if len(resultArray) != 0: #결과 배열 안 비어있음
        topNo = resultArray[-1]
        #인형 삭제
        if topNo == no:
          resultArray.pop()
          return 2
        #인형 삭제 실패 (누적)
        else:
            resultArray.append(no)
            return 0
    if len(resultArray) == 0: #결과 배열 비어있음
        resultArray.append(no)
        return 0
