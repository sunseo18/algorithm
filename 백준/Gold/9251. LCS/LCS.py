import sys

a = sys.stdin.readline().strip()
b = sys.stdin.readline().strip()


a_length = len(a)
b_length = len(b)


dp = [[0 for _ in range(a_length+1)] for _ in range(b_length+1)]

for i in range(1, b_length+1):
    for j in range(1, a_length+1):
        if b[i-1] == a[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])


        
print(dp[i][j])
