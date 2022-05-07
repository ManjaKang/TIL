N = int(input())
dp = [0] * (N+1)
dp[1] = 9
for i in range(2, N+1):
    dp[i] = dp[i-1] + 7
print(dp[N])