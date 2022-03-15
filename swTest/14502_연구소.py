import copy


def comb_dfs(s):
    if len(temp_list) == 3:
        case_list.append(temp_list[:])
        return

    for idx in range(s, len(space_list)):
        now = space_list[idx]
        if space_arr[now[0]][now[1]] == 1:
            space_arr[now[0]][now[1]] = 2
            temp_list.append(now)
            comb_dfs(idx+1)
            space_arr[now[0]][now[1]] = 1
            temp_list.pop()


def virus_dfs():
    global min_cnt
    global cnt
    cnt = 0
    temp_vi_list = copy.deepcopy(virus_list)
    temp_arr = copy.deepcopy(arr)
    while temp_vi_list:
        now = temp_vi_list.pop()
        for idx in range(4):
            ni = now[0] + di[idx]
            nj = now[1] + dj[idx]
            if (0 <= ni < N) and (0 <= nj < M) and (temp_arr[ni][nj] == 0):
                temp_arr[ni][nj] = 2
                cnt += 1
                temp_vi_list.append((ni, nj))
        if min_cnt <= cnt:
            return False
    return True


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
# 입력 끝

space_list = []
space_arr = [[0]*M for _ in range(N)]
temp_list = []
virus_list = []
case_list = []
num_space = 0
min_cnt = 100
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
cnt = 0
# 변수 선언 끝

for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            space_arr[i][j] = 1
            space_list.append((i, j))
            num_space += 1
        elif arr[i][j] == 2:
            virus_list.append((i, j))
# 변수 저장 끝

comb_dfs(0)
for case in case_list:
    for point in case:
        arr[point[0]][point[1]] = 1
    if virus_dfs():
        min_cnt = cnt
    for point in case:
        arr[point[0]][point[1]] = 0
print(num_space - min_cnt - 3)