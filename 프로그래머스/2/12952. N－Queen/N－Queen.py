def promising(A, r, c):
    # A로 나타내어진 지금 체스판 상태에서,
    # r행의 c열에 퀸을 둘수 있는지 없는지 판단합니다.
    # 1. c열에 퀸이 있으면 안됩니다.
    if c in A[:r]:
        return False
    # 2. 왼쪽 대각선 위에 퀸이 있으면 안됩니다.
    for dr in range(1, r+1):
        if c-dr >= 0 and r-dr >= 0:
            if A[r-dr] == c-dr:
                return False
    # 3. 오른쪽 대각선 위에 퀸이 있으면 안됩니다.
    for dr in range(1, r+1):
        if c+dr < len(A) and r-dr >= 0:
            if A[r-dr] == c+dr:
                return False
    return True

def solve(A, r):
    # n+1행까지 왔다는 건 체스판이 완성되었다는 것이므로
    # 경우의 수 하나 추가
    if r == len(A):
        return 1
    # 체스판 상태 A의 r행에 퀸을 둬봅니다.
    ans = 0
    for c in range(len(A)):
        if promising(A, r, c):  # r행 c열에 퀸을 둬도 되면
            A[r] = c
            ans += solve(A, r+1)
            A[r] = -1
            
    return ans

def solution(n):
    # 길이 n짜리 배열 A를 만들어 둡니다.
    # A[i]는 i번째 행에 퀸이 놓인 열의 index입니다.
    A = [-1] * n
    return solve(A, 0)