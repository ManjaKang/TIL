from collections import deque


def roll(direct):
    global i, j, op_num
    if direct == 1:
        que_row.appendleft(op_num)
        op_num = que_row.pop()
        que_col[1] = que_row[1]
    if direct == 2:
        que_row.append(op_num)
        op_num = que_row.popleft()
        que_col[1] = que_row[1]
    if direct == 3:
        que_col.appendleft(op_num)
        op_num = que_col.pop()
        que_row[1] = que_col[1]
    if direct == 4:
        que_col.append(op_num)
        op_num = que_col.popleft()
        que_row[1] = que_col[1]
    if arr[i][j] == 0:
        arr[i][j] = op_num
    else:
        op_num = arr[i][j]
        arr[i][j] = 0


def move(direct):
    global i, j
    di = [0, 0, 0, -1, 1]
    dj = [0, 1, -1, 0, 0]
    ni = i + di[direct]
    nj = j + dj[direct]
    if (0 <= ni < N) and (0 <= nj < M):
        i, j = ni, nj
        return True
    else:
        return False


N, M, si, sj, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
k_list = list(map(int, input().split()))
# 입력 끝


que_row = deque([0, 0, 0])
que_col = deque([0, 0, 0])
op_num = 0
i, j = si, sj
# 변수 선언 끝

for k in k_list:
    if move(k):
        roll(k)
        print(que_row[1])
