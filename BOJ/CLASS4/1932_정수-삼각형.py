def dfs(i, n, s):
    global ans
    if (N-n) * max_num + s < ans:
        return

    if n == N:
        ans = max(ans, s)
        return

    dfs(i, n+1, s+arr[n][i])
    dfs(i+1, n+1, s+arr[n][i])


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
max_num = max(sum(arr, []))
ans = 0
dfs(0, 0, 0)
print(ans)