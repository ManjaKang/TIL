
def bfs():
    global stack
    global cnt
    for idx in range(6):
        ni = i + di[idx]
        nj = j + dj[idx]
        nk = k + dk[idx]
        if (0 <= ni < H) and (0 <= nj < N) and (0 <= nk < M) and (arr[ni][nj][nk] == 0):
            arr[ni][nj][nk] = 1
            cnt += 1
            dfs(ni, nj, nk)
            cnt -= 1
    return
# 함수 선언 끝


M, N, H = map(int, input().split())
arr = [[list(map(int, input().split())) for _ in range(N)] for __ in range(H)]
# 입력 끝

di = [0, 0, 0, 0, -1, 1]
dj = [0, 1, 0, -1, 0, 0]
dk = [1, 0, -1, 0, 0, 0]
stack = []
cnt = 0
# 변수 선언 끝

for i in range(H):
    for j in range(N):
        for k in range(M):
            if arr[i][j][k] == 1:
                stack.append((i, j, k))

print(dfs())