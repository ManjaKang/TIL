# PyPy 528ms


def dust_diffusion(arr):
    temp_arr = [[0]*C for _ in range(R)]
    temp_arr[air_cleaner][0] = -1
    temp_arr[air_cleaner+1][0] = -1
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    for i in range(R):
        for j in range(C):
            if arr[i][j] > 0:
                temp_arr[i][j] += arr[i][j]
                dust = arr[i][j] // 5
                for idx in range(4):
                    ni = i + di[idx]
                    nj = j + dj[idx]
                    if 0 <= ni < R and 0 <= nj < C and arr[ni][nj] != -1:
                        temp_arr[ni][nj] += dust
                        temp_arr[i][j] -= dust
    return temp_arr


# 윗쪽 공기 순환 함수
def top_dfs(i, j, d):
    ni = i + di_t[d]
    nj = j + dj_t[d]
    if 0 <= ni <= air_cleaner and 0 <= nj < C:
        if dust_arr[ni][nj] == -1:
            dust_arr[i][j] = 0
            return
        dust_arr[i][j] = dust_arr[ni][nj]
        top_dfs(ni, nj, d)
    else:
        top_dfs(i, j, d+1)
    return


# 아랫쪽 공기 순환 함수
def bottum_dfs(i, j, d):
    ni = i + di_d[d]
    nj = j + dj_d[d]
    if air_cleaner < ni < R and 0 <= nj < C:
        if dust_arr[ni][nj] == -1:
            dust_arr[i][j] = 0
            return
        dust_arr[i][j] = dust_arr[ni][nj]
        bottum_dfs(ni, nj, d)
    else:
        bottum_dfs(i, j, d+1)
    return


R, C, T = map(int, input().split())
dust_arr = [list(map(int, input().split())) for _ in range(R)]
# 입력 끝

di_t = [-1, 0, 1, 0]
dj_t = [0, 1, 0, -1]
di_d = [1, 0, -1, 0]
dj_d = [0, 1, 0, -1]

# 공기 청정기 위치 찾기
for i in range(R):
    if dust_arr[i][0] == -1:
        air_cleaner = i
        break

# T초간 시뮬레이션
for _ in range(T):
    dust_arr = dust_diffusion(dust_arr)
    top_dfs(air_cleaner-1, 0, 0)
    bottum_dfs(air_cleaner+2, 0, 0)

ans = 2
for dust in dust_arr:
    ans += sum(dust)
print(ans)

