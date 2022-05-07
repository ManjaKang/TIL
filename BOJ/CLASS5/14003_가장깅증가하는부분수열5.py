import bisect

N = int(input())
arr = [0] + list(map(int, input().split()))
memo = [arr[-1]]
dp = [0] * (N + 1)
for i in range(1, N + 1):
    if memo[-1] < arr[i]:
        memo.append(arr[i])
        dp[i] = len(memo) - 1
    else:
        dp[i] = bisect.bisect_left(memo, arr[i])
        memo[dp[i]] = arr[i]

max_idx = max(dp) + 1
ans = []
for i in range(N, 0, -1):
    if dp[i] == max_idx - 1:
        max_idx = dp[i]
        ans.append(arr[i])
print(len(ans))
print(*ans[::-1])
