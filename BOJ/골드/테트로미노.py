def dfs(i, j, cnt, ratio, s):
    global max_ratio
    global ans
    # 가지치기
    if max_ratio > ratio:
        return
    # 종료 조건
    if cnt == 3:
        if max_ratio < ratio:
            max_ratio = ratio
            ans = s
        return
    for idx in range(4):
        ni = i + di[idx]
        nj = j + dj[idx]
        if (0 <= ni < N) and (0 <= nj < M) and visited[ni][nj] == 0:
            visited[ni][nj] = 1
            dfs(ni, nj, cnt + 1, ratio * arr[ni][nj] / 1000, s+arr[ni][nj])
            visited[ni][nj] = 0


#  ㅜ 모양 합 구하기
def bfs(i, j):
    global ans
    s = arr[i][j]
    cnt = 0
    min_s = 10000
    for idx in range(4):
        ni = i + di[idx]
        nj = j + dj[idx]
        if (0 <= ni < N) and (0 <= nj < M):
            cnt += 1
            s += arr[ni][nj]
            if min_s > arr[ni][nj]:
                min_s = arr[ni][nj]
    if cnt <= 2:
        return
    if cnt == 4:
        s -= min_s
    if ans < s:
        ans = s


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
# 입력 끝

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
visited = [[0] * M for _ in range(N)]
max_ratio = 0
ans = 0
for i in range(N):
    for j in range(M):
        visited[i][j] = 1
        dfs(i, j, 0, arr[i][j] / 1000, arr[i][j])
        visited[i][j] = 0
for i in range(N):
    for j in range(M):
        bfs(i, j)
print(ans)
