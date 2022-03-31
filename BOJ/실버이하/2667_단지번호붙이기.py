def dfs(i, j):
    if (i < 0) or (i >= N) or (j < 0) or (j >= N):
        return False
    if arr[i][j] == 1:
        global cnt
        cnt += 1
        arr[i][j] = 0
        for idx in range(4):
            ni = i + di[idx]
            nj = j + dj[idx]
            dfs(ni, nj)
        return True
    return False


N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
# 입력 끝

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
stack = []
ans_list = []
cnt = 0
# 글로벌 변수 선언 끝

for i in range(N):
    for j in range(N):
        if dfs(i, j):
            ans_list.append(cnt)
            cnt = 0
ans_list.sort()
# 풀이 끝

print(len(ans_list))
print(*ans_list, sep='\n')