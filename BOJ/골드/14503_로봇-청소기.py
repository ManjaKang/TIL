def clean(i, j, d, n):
    global cnt

    while True:
        # 현재 위치 청소
        if arr[i][j] == 0:
            arr[i][j] = 2
            cnt += 1
            n = 0
        # 4회 반복시
        if n == 4:
            ni = i + di[(d + 2) % 4]
            nj = j + dj[(d + 2) % 4]
            # 뒤가 벽이면 종료
            if arr[ni][nj] == 1:
                return
            # 후진
            else:
                i = ni
                j = nj
                n = 0
                continue
        # 왼쪽 탐색
        nd = (d - 1) % 4
        ni = i + di[nd]
        nj = j + dj[nd]
        if arr[ni][nj] == 0:
            i = ni
            j = nj
            d = nd
            n = 0
            continue
        else:
            d = nd
            n += 1
            continue


di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
N, M = map(int, input().split())
r, c, d = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
# 입력 끝

cnt = 0

clean(r, c, d, 0)
print(cnt)
