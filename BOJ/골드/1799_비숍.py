def dfs(s, n):
    i, j = stack[s]
    x1 = i + j
    x2 = i - j + N - 1
    visited_r[x1] = 1
    visited_l[x2] = 1
    global ans
    if ans < n:
        ans = n

    for a in range(s+1, len(stack)):
        i, j = stack[a]
        x1 = i + j
        x2 = i - j + N - 1
        if visited_r[x1] == 0 and visited_l[x2] == 0:
            dfs(a, n+1)


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
stack = []
ans = 0
visited_r = [0] * (2 * N - 1)
visited_l = [0] * (2 * N - 1)
for i in range(N):
    for j in range(N):
        if arr[i][j]:
            stack.append((i, j))

for a in range(len(stack)):
    dfs(a, 1)

print(ans)