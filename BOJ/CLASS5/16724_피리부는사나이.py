N, M = map(int, input().split())
arr = [input() for _ in range(N)]

move_dict = {
    'D': (1, 0),
    'L': (0, -1),
    'U': (-1, 0),
    'R': (0, 1),
}
visited = [[0]*M for _ in range(N)]
idx = 0
ans = 0


def dfs(i, j):
    global idx
    di, dj = move_dict[arr[i][j]]
    ni = i + di
    nj = j + dj
    if visited[ni][nj] == 0:
        visited[ni][nj] = idx
        dfs(ni, nj)
    elif visited[ni][nj] != idx:
        global ans
        ans -= 1


for i in range(N):
    for j in range(M):
        if visited[i][j] == 0:
            ans += 1
            idx += 1
            dfs(i, j)

print(ans)
