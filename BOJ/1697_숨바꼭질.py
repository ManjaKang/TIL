def enQue(v):
    global front
    que.append(v)
    front += 1
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
    enQue(N)
    visited[N] = 1
    while not isEmpty():
        now = deQue()
        if now == K:
            break
        if (0 <= now*2 < 100001) and (visited[now*2] == 0):
            visited[now*2] = visited[now] + 1
            enQue(now*2)
        if (0 <= now+1 < 100001) and (visited[now+1] == 0):
            visited[now+1] = visited[now] + 1
            enQue(now+1)
        if (0 <= now-1 < 100001) and (visited[now-1] == 0):
            visited[now-1] = visited[now] + 1
            enQue(now-1)
    return visited[K] - 1


N, K = map(int, input().split())
# 입력 끝

que = []
front = -1
rear = -1
visited = [0] * 100001
# 변수 선언 끝

ans = bfs()
print(ans)
