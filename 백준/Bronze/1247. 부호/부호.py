for _ in range(3):
    sum = 0
    N = int(input())
    for i in range(N):
        sum += int(input())

    if sum < 0:
        print('-')
    elif sum > 0:
        print('+')
    else:
        print('0')

    