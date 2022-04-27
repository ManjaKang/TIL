N = int(input())
arr = [0] * N
for i in range(N):
    arr[i] = list(map(int, input().split()))

dp = [[0]*i for i in range(1, N+1)]
dp[-1] = arr[-1]
for i in range(N-2, -1, -1):
    for j in range(i+1):
        dp[i][j] = max(dp[i+1][j], dp[i+1][j+1]) + arr[i][j]
print(dp[0][0])