def getScoreWithArea(area, score):
    if area == 'S':
        return score
    elif area == 'D':
        return score*score
    elif area == 'T':
        return score*score*score

        
def solution(dartResult):
    dartResultList = list(dartResult)
    resultStack = []
    
    area = ['S', 'D', 'T']
    option = ['*', '#']

    i = -1
    for j in range(1, len(dartResultList)):
        if dartResultList[j] in area:
            resultStack.append(getScoreWithArea(dartResultList[j], int("".join(dartResultList[i+1:j]))))
            i = j
            
        if dartResultList[j] == '*':
            lastTwoOfStack = resultStack[-2:]
            del resultStack[-2:]
            for l in lastTwoOfStack:
                resultStack.append(l*2)
            i = j
            
        if dartResultList[j] == '#':
            lastOfStack = resultStack.pop()
            resultStack.append(lastOfStack * -1)
            i = j

    return sum(resultStack)
