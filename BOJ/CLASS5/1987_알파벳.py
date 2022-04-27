def dfs(i, j, word):
    global ans
    if ans < len(word):
        ans = len(word)
    for idx in range(4):
        ni = i + di[idx]
        nj = j + dj[idx]
        if 0 <= ni < R and 0 <= nj < C and arr[ni][nj] not in word:
            dfs(ni, nj, word+arr[ni][nj])


R, C = map(int, input().split())
arr = [input() for _ in range(R)]
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
ans = 0
dfs(0, 0, arr[0][0])

print(ans)