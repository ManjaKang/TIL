# PyPy 312ms
from collections import defaultdict

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]


def check():
    stack = [(0, 0)]
    visited = defaultdict(lambda: defaultdict(int))
    visited[0][0] = 1
    check_dict = defaultdict(lambda: defaultdict(int))
    flag = False
    while stack:
        i, j = stack.pop()
        for idx in range(4):
            ni = i + di[idx]
            nj = j + dj[idx]
            if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 0:
                if arr[ni][nj]:
                    check_dict[ni][nj] += 1
                else:
                    visited[ni][nj] = 1
                    stack.append((ni, nj))
    for i, j_dict in check_dict.items():
        for j, val in j_dict.items():
            if val >= 2:
                arr[i][j] = 0
                flag = True
    if flag:
        return True
    return False


ans = 0
while check():
    ans += 1

print(ans)
