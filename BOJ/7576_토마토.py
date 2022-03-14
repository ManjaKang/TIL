def isFull():
    if front == size:
        return True
    return False


def isEmpty():
    if front == rear:
        return True
    return False


def deQue():
    global rear
    if isEmpty():
        print('Full')
        return 0
    rear += 1
    return que[rear]


def enQue(value):
    global front
    global size
    if isFull():
        size += create
        que.extend([0]*create)
    front += 1
    que[front] = value
    return


def bfs():
    global day
    global change
    temp_list = []

    for a in arr:
        if 0 in a:
            break
    else:
        return 0
    while change:
        change = False
        while not isEmpty():
            now = deQue()
            arr[now[0]][now[1]] = 1
            for idx in range(4):
                ni = now[0] + di[idx]
                nj = now[1] + dj[idx]
                if (0 <= ni < N) and (0 <= nj < M) and (arr[ni][nj] == 0):
                    arr[ni][nj] = 1
                    change = True
                    temp_list.append((ni, nj))
        for temp in temp_list:
            enQue(temp)
        if change:
            day += 1
        temp_list = []
    for a in arr:
        if 0 in a:
            return -1
    return day


M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
# 입력 끝

size = 1000000
create = 1000
que = [0]*size
front = -1
rear = -1
day = 0
change = True
flag = False
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
# 변수 선언 끝

for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            enQue((i, j))

ans = bfs()
print(ans)
