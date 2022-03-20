def enQue(v):
    global front
    global size
    global que
    global create
    if front == size - 1:
        que += [0] * create
        size += create
    front += 1
    que[front] = v
    return


def deQue():
    global rear
    rear += 1
    return que[rear]


def isEmpty():
    if rear == front:
        return True
    return False


def bfs():
    cnt = 0
    flag = True
    day = 0
    while not isEmpty():
        i, j, k = deQue()
        for idx in range(6):
            ni = i + di[idx]
            nj = j + dj[idx]
            nk = k + dk[idx]
            if (0 <= ni < H) and (0 <= nj < N) and (0 <= nk < M) and (arr[ni][nj][nk] == 0):
                arr[ni][nj][nk] = arr[i][j][k] + 1
                cnt += 1
                enQue((ni, nj, nk))
                if day < arr[ni][nj][nk]:
                    day = arr[ni][nj][nk]
    if cnt0 == 0:
        return 0
    if cnt0 != cnt:
        return -1
    return day - 1
# 함수 선언 끝


M, N, H = map(int, input().split())
arr = [[list(map(int, input().split())) for _ in range(N)] for __ in range(H)]
# 입력 끝

di = [0, 0, 0, 0, -1, 1]
dj = [0, 1, 0, -1, 0, 0]
dk = [1, 0, -1, 0, 0, 0]
size = 10000
create = 1000
que = [0] * size
temp_stack = []
cnt0 = 0
front = -1
rear = -1
# 변수 선언 끝

for i in range(H):
    for j in range(N):
        for k in range(M):
            if arr[i][j][k] == 1:
                enQue((i, j, k))
            elif arr[i][j][k] == 0:
                cnt0 += 1

ans = bfs()
print(ans)
