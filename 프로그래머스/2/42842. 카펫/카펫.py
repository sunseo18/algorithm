def solution(brown, yellow):
    
    for x in range(1, yellow+1):
        left = yellow % x
        if left == 0:
            y = yellow / x

            if (x * 2 + y * 2 + 4) == brown:
                return [max(x, y) + 2, min(x, y) + 2]
