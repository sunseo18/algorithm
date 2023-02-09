n = int(input())
cards = sorted(list(map(int, input().split())))
m = int(input())
checkCards = list(map(int, input().split()))

def binSearch(minIndex, maxIndex, card):
    if maxIndex < minIndex:
        return False
    
    midIndex = (minIndex + maxIndex)//2
    if card == cards[midIndex]:
        return True
    
    elif card < cards[midIndex]:
        return binSearch(minIndex, midIndex-1, card)

    else:
        return binSearch(midIndex+1, maxIndex, card)

for card in checkCards:
    if binSearch(0, n-1, card):
        print("1", end=" ")
    else: 
        print("0", end=" ")
