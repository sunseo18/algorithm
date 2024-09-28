import sys

sys.setrecursionlimit(10**6)

length = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))

question = int(sys.stdin.readline())

dp = [[-1 for _ in range(length)] for _ in range(length)]


def calculate(i, j):
    if i == j:
        dp[i][j] = 1
        return 1
    
    if dp[i][j] != -1:
        return dp[i][j]

    # 몰라서 새로 구해야되는 값
    if dp[i][j] == -1:
        # 양 끝 값이 같으면 내부 검사 필요
        if numbers[i] == numbers[j]:
            # 인덱스가 하나 차이면 문자열 비교
            if j - i == 1:
                # 두 개가 같으면 1 저장
                if numbers[i] == numbers[j]:
                    dp[i][j] = 1
                    return 1
                # 두 개가 다르면 0 저장
                else:
                    dp[i][j] = 0
                    return 0
            # 인덱스가 하나 차이가 아니면 양끝 하나씩 좁힌 거 검사
            dp[i][j] = calculate(i+1, j-1)
        # 양 끝 값이 다르면 무조건 0
        else:
            dp[i][j] = 0

    return dp[i][j]
    
    

for _ in range(question):
    S, E = map(int, sys.stdin.readline().split())
    sys.stdout.write(str(calculate(S-1, E-1)))
    sys.stdout.write('\n')

