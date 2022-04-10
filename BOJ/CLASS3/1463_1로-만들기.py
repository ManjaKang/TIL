import collections


def dfs(n, c):
    global ans
    if ans < c:
        return
    if n == 1:
        ans = min(ans, c)
        return

    if not n % 3:
        if visited[n/3] > c:
            visited[n/3] = c
            dfs(n/3, c+1)
    if not n % 2:
        if visited[n/2] > c:
            visited[n/2] = c
            dfs(n/2, c+1)
    if visited[n-1] > c:
        visited[n-1] = c
        dfs(n-1, c+1)


X = int(input())
ans = 100000000
visited = collections.defaultdict(lambda: 100000000)
dfs(X, 0)
print(ans)