N = int(input())
arr = [int(input()) for _ in range(N)]
dp = [0] * N
if N == 1:
    print(arr[0])
elif N == 2:
    print(arr[0]+arr[1])
else:
    dp[0] = arr[0]
    dp[1] = arr[0] + arr[1]
    dp[2] = max(arr[2]+arr[0], arr[2]+arr[1], dp[1])
    for i in range(3, N):
        dp[i] = max(arr[i]+dp[i-2], arr[i]+arr[i-1]+dp[i-3], dp[i-1])
    print(max(dp))