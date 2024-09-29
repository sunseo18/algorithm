import sys

input = sys.stdin.readline

R_INDEX = 0
G_INDEX = 1
B_INDEX = 2
INF = float('inf')

n = int(input())

rgb = []
for _ in range(n):
    rgb.append(list(map(int, input().split())))


dp = [[(rgb[0][R_INDEX], INF, INF), (INF, rgb[0][G_INDEX], INF), (INF, INF, rgb[0][B_INDEX])]]


for i in range(1, n):
    tmp = []
    for j in range(3):
        if j == R_INDEX:
            next_R = min(dp[i-1][G_INDEX][R_INDEX], dp[i-1][B_INDEX][R_INDEX])
            next_G = min(dp[i-1][G_INDEX][G_INDEX], dp[i-1][B_INDEX][G_INDEX])
            next_B = min(dp[i-1][G_INDEX][B_INDEX], dp[i-1][B_INDEX][B_INDEX])  
            tmp.append((next_R+rgb[i][j], next_G+rgb[i][j], next_B+rgb[i][j]))
            
        elif j == G_INDEX:
            next_R = min(dp[i-1][R_INDEX][R_INDEX], dp[i-1][B_INDEX][R_INDEX])
            next_G = min(dp[i-1][R_INDEX][G_INDEX], dp[i-1][B_INDEX][G_INDEX])
            next_B = min(dp[i-1][R_INDEX][B_INDEX], dp[i-1][B_INDEX][B_INDEX])  
            tmp.append((next_R+rgb[i][j], next_G+rgb[i][j], next_B+rgb[i][j]))
            
        else:
            next_R = min(dp[i-1][R_INDEX][R_INDEX], dp[i-1][G_INDEX][R_INDEX])
            next_G = min(dp[i-1][R_INDEX][G_INDEX], dp[i-1][G_INDEX][G_INDEX])
            next_B = min(dp[i-1][R_INDEX][B_INDEX], dp[i-1][G_INDEX][B_INDEX])  
            tmp.append((next_R+rgb[i][j], next_G+rgb[i][j], next_B+rgb[i][j]))
    dp.append(tmp)


print (
    min ( min(dp[n-1][R_INDEX][B_INDEX], dp[n-1][R_INDEX][G_INDEX]),
      min(dp[n-1][G_INDEX][R_INDEX], dp[n-1][G_INDEX][B_INDEX]),
      min(dp[n-1][B_INDEX][R_INDEX], dp[n-1][B_INDEX][G_INDEX]))
    )



        
