from copy import deepcopy


# 해당 방향으로 CCTV 설치
def watch(dirs, i, j):
    for direct in dirs:
        ni = i
        nj = j
        while True:
            ni += di[direct]
            nj += dj[direct]
            if (0 <= ni < N) and (0 <= nj < M) and (arr[ni][nj] != 6):
                if arr[ni][nj] == 0:
                    arr[ni][nj] = 7
            else:
                break
    return


def dfs(n):
    global arr
    if n == len(cctv_list):
        count = 0
        global min_value
        for i in range(N):
            count += arr[i].count(0)
        min_value = min(min_value, count)
        return
    temp = deepcopy(arr)
    cctv_type, i, j = cctv_list[n]
    for dirs in type_dict[cctv_type]:
        watch(dirs, i, j)
        dfs(n+1)
        arr = deepcopy(temp)


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
cctv_list = []
for i in range(N):
    for j in range(M):
        if arr[i][j] != 0 and arr[i][j] != 6:
            cctv_list.append([arr[i][j], i, j])
# 입력 끝

type_dict = {
    1: [[0], [1], [2], [3]],
    2: [[0, 2], [1, 3]],
    3: [[0, 1], [1, 2], [2, 3], [0, 3]],
    4: [[0, 1, 2], [0, 1, 3], [1, 2, 3], [0, 2, 3]],
    5: [[0, 1, 2, 3]],
}
#     북 동 남 서
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
min_value = int(1e9)

dfs(0)
print(min_value)