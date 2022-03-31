def dfs(n, s):
    global max_s
    # 종료 조건
    if n > N:
        return
    if n == N:
        if max_s < s:
            max_s = s
        return
    dfs(n + 1, s)
    dfs(n + arr[n][0], s + arr[n][1])


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
max_s = 0
dfs(0, 0)
print(max_s)
