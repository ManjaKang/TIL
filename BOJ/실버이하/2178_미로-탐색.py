def isFull():
    global front
    global size
    if front == size-1:
        return True
    return False


def isEmpty():
    global front
    global rear
    if front == rear:
        return True
    return False


def deQue():
    global rear
    if isEmpty():
        return 0
    rear += 1
    return que[rear]


def enQue(value):
    global front
    global size
    global que
    if isFull():
        size += create
        que += [0]*create
    front += 1
    que[front] = value
    return


def bfs():
    global cnt
    enQue((0, 0))
    while not isEmpty():
        now = deQue()
        if now == (N-1, M-1):
            return arr[now[0]][now[1]]
        for idx in range(4):
            ni = now[0] + di[idx]
            nj = now[1] + dj[idx]
            if (0 <= ni < N) and (0 <= nj < M) and (arr[ni][nj] == 1):
                enQue((ni, nj))
                arr[ni][nj] = arr[now[0]][now[1]] + 1
    return 0


N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
# 입력 끝

size = 1000
create = 100
que = [0] * size
front = -1
rear = -1
cnt = 1
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
ans = 0
# 변수 선언 끝

ans = bfs()
print(ans)

