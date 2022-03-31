def enQue(v):
    global front
    front += 1
    que.append(v)
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
    enQue(S)
    visited[S] = 1
    while not isEmpty():
        now = deQue()
        if now == G:
            break
        if (1 <= now+U < F+1) and (visited[now+U] == 0):
            visited[now+U] = visited[now] + 1
            enQue(now+U)
        if (1 <= now-D < F+1) and (visited[now-D] == 0):
            visited[now-D] = visited[now] + 1
            enQue(now-D)
    else:
        return 'use the stairs'
    return visited[G] - 1


F, S, G, U, D = map(int, input().split())
# 입력 끝

que = []
front = -1
rear = -1
visited = [0] * (F+1)
# 변수 선언 끝

ans = bfs()
print(ans)