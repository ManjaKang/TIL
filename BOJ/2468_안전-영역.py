def dfs(n):
    while stack:
        i, j = stack.pop()
        for idx in range(4):
            ni = i + di[idx]
            nj = j + dj[idx]
            if (0 <= ni < N) and (0 <= nj < N) and (visited[ni][nj] == 0) and (arr[ni][nj] > n):
                visited[ni][nj] = 1
                stack.append((ni, nj))
    return


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
# 입력 끝

# 가장 높은 지역 찾기
max_h = 0
for ar in arr:
    for a in ar:
        if max_h < a:
            max_h = a

stack = []
di = [0, -1, 0, 1]
dj = [1, 0, -1, 0]
cnt = 0
max_cnt = 0
# 변수 선언 긑

for n in range(max_h):
    cnt = 0
    visited =[[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if (visited[i][j] == 0) and (arr[i][j] > n):
                stack.append((i, j))
                visited[i][j] = 1
                dfs(n)
                cnt += 1
    if max_cnt < cnt:
        max_cnt = cnt

print(max_cnt)