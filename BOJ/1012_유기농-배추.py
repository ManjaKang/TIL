from pprint import pprint


def dfs(i, j):
    if arr[i][j] == 0:
        return False
    stack.append((i, j))
    arr[i][j] = 0
    while stack:
        now = stack.pop()
        for idx in range(4):
            ni = now[0] + di[idx]
            nj = now[1] + dj[idx]
            if (0 <= ni < N) and (0 <= nj < M) and (arr[ni][nj] == 1):
                stack.append((ni, nj))
                arr[ni][nj] = 0
    return True


T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    arr = [[0] * M for _ in range(N)]
    for _ in range(K):
        i, j = map(int, input().split())
        arr[i][j] = 1
    # 입력 끝

    cnt = 0
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    stack = []
    # 변수 선언 끝

    for i in range(N):
        for j in range(M):
            if dfs(i, j):
                cnt += 1
    pprint(cnt)
