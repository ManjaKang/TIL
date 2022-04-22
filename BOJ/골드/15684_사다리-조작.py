from pprint import pprint
from itertools import combinations
from copy import deepcopy


def game(n):
    visited = [[0]*N for _ in range(H+1)]
    i = 0
    j = n
    visited[i][j] = 1
    while True:
        ni = i + di[arr[i][j]]
        nj = j + dj[arr[i][j]]
        if visited[ni][nj] == 0:
            i = ni
            j = nj
        else:
            i = i + 1
        visited[i][j] = 1
        if i == H:
            if j == n:
                return True
            else:
                return False


def dfs(n):
    global ans
    if n >= ans:
        return

    for i in range(N):
        if not game(i):
            break
    else:
        ans = n
        return

    for i in range(H):
        for j in range(N-1):
            if arr[i][j] == 0:
                arr[i][j] = 1
                arr[i][j+1] = 2
                dfs(n+1)
                arr[i][j] = 0
                arr[i][j+1] = 0


N, M, H = map(int, input().split())
arr = [[0]*N for _ in range(H)]
di = [1, 0, 0]
dj = [0, 1, -1]
ans = 4
end = False

for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    arr[a][b] = 1
    arr[a][b+1] = 2

dfs(0)
if ans == 4:
    ans = -1
print(ans)
