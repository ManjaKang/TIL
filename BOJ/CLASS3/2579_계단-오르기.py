import collections


def dfs(n, s, c):
    if n > N+1:
        return
    if n == N+1:
        global ans
        ans = max(ans, s)
        return

    if c == 2:
        dfs(n+2, s+arr[n], 1)
    else:
        dfs(n+1, s+arr[n], c+1)
        dfs(n+2, s+arr[n], 1)


N = int(input())
arr = [int(input()) for _ in range(N)]
arr.insert(0, 0)
ans = 0
visited = collections.defaultdict(int)
dfs(0, 0, 0)
print(ans)