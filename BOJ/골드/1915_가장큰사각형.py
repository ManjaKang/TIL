def check(i, j):
    for a in range(v+1):
        ni = i + a
        if ni < N:
            for b in range(v+1):
                nj = j + b
                if nj < M:
                    if arr[ni][nj] != 0:
                        continue
                    else:
                        return False
                else:
                    return False
        else:
            return False
    global stack
    arr[


N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
stack = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            stack.append((i, j))

while stack:
    i, j = stack.pop()
    v = arr[i][j]
    for a in range(v+1):
        ni = i + a
        if ni < N:
            for b in range(v+1):
                nj = j + b
                if nj < M:
                    if arr[ni][nj] != 0:
                        continue


