# PyPy: 2244ms
from collections import deque


def bfs(i, j):
    sum_p = arr[i][j]
    visited[i][j] = 1
    united = [(i, j)]
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    que = deque([(i, j)])
    while que:
        i, j = que.popleft()
        for idx in range(4):
            ni = i + di[idx]
            nj = j + dj[idx]
            if (0 <= ni < N) and (0 <= nj < N):
                if visited[ni][nj] == 0 and L <= abs(arr[i][j] - arr[ni][nj]) <= R:
                    visited[ni][nj] = 1
                    que.append((ni, nj))
                    united.append((ni, nj))
                    sum_p += arr[ni][nj]
    p = sum_p // len(united)
    for i, j in united:
        arr[i][j] = p
    if len(united) > 1:
        return True
    return False


N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

cnt = 0
move = True
while move:
    visited = [[0]*N for _ in range(N)]
    move = False
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                if bfs(i, j):
                    move = True
    if move:
        cnt += 1
print(cnt)

