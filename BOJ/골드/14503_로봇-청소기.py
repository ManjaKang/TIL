def clean(i, j, d, n):
    global cnt
    if arr[i][j] == 0:
        arr[i][j] = 1
        cnt += 1
        n = 0
    else:
        n += 1
    if n == 4:
        return
    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]
    nd = (d - 1) % 4
    ni = i + di[nd]
    nj = j + dj[nd]
    if (0 <= ni < N) and (0 <= nj < M) and (arr[ni][nj] == 0):
        clean(ni, nj, nd, 0)
    else:
        clean(i, i, nd, n+1)


N, M = map(int, input().split())
r, c, d = map(int, input().split())
r -= 1
c -= 1
arr = [list(map(int, input().split())) for _ in range(N)]
# 입력 끝

cnt = 0

clean(r, c, d, 0)
print(cnt)

