def dfs():
    stack.append((R, B, 0))
    visited.append((R, B))
    while stack:
        r, bl, cnt = stack.pop(0)
        i = r[0]
        j = r[1]
        a = bl[0]
        b = bl[1]
        cnt_dot = 0
        flag = False
        for idx in range(4):
            cnt_dot = 0
            for n in range(1, H):
                ni = a + di[idx] * n
                nj = b + dj[idx] * n
                if arr[ni][nj] == 'O':
                    flag = True
                    break
                elif arr[ni][nj] == '#':
                    ni = i + di[idx] * cnt_dot
                    nj = j + dj[idx] * cnt_dot
                    temp1 = (ni, nj)
                    break
                elif arr[ni][nj] == '.':
                    cnt_dot += 1
            if flag:
                break

            for n in range(1, H):
                ni = i + di[idx] * n
                nj = j + dj[idx] * n
                if arr[ni][nj] == 'O':
                    return cnt
                elif arr[ni][nj] == '#':
                    ni = i + di[idx] * cnt_dot
                    nj = j + dj[idx] * cnt_dot
                    temp2 = (ni, nj)
                    break
                elif arr[ni][nj] == '.':
                    cnt_dot += 1

            if (temp1, temp2) not in visited:
                visited.append((temp1, temp2))
                stack.append((temp1, temp2, cnt + 1))


N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
H = max(N, M)
# 입력 끝

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
ans = 0
stack = []
visited = []
# 변수 선언 끝

for i in range(N):
    for j in range(M):
        if arr[i][j] == 'B':
            B = (i, j)
        if arr[i][j] == 'R':
            R = (i, j)
        if arr[i][j] == 'O':
            O = (i, j)

ans = dfs()

print(arr)