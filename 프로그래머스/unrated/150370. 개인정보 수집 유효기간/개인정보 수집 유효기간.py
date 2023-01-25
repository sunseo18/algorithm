def solution(today, terms, privacies):
    privacyTermArr = []   #term 배열로 추출한 것
    termDaysDict = dict() #term, 개월 수 날짜로 변경한 것 저장
    privacyArr = [] #privacy 날짜 추출한 것
    privacyDays = [] #privacy날짜 day로 변경한 배열
    answer = []

    todayToDays = dateToDays(today)

    for privacy in privacies:
        splitArr = privacy.split(" ")

        privacyTermArr.append( splitArr)

    for privacy in privacyTermArr:
        privacyDays.append(dateToDays(privacy[0]))


    for term in terms:
        splitArr = term.split(" ")
        termDaysDict[splitArr[0]] = int(splitArr[1])*28


    for i in range(len(privacyTermArr)):

        privacyPlusTerm = termDaysDict[privacyTermArr[i][1]] + privacyDays[i]
        if privacyPlusTerm <= todayToDays:
            answer.append(i+1)
        

    return answer

def dateToDays(date):
    daysArr = date.split(".")
    yearDays = (int(daysArr[0]) - 2000) * 28 *12
    monthDays = (int(daysArr[1]) - 1) * 28
    days = (int(daysArr[2]) - 1)

    return  yearDays + monthDays + days
