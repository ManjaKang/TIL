import sys
sys.stdin = open('sample_input.txt', 'r')


def dfs_comb(i, j):
    if len(now) == 2:
        if not (now[0][0] == now[1][0] and abs(now[0][1] - now[1][1]) < M):
            case_list.append(now[:])
        return
    for ni in range(i, N):
        for nj in range(N-M+1):
            if visited[ni][nj] == 0:
                visited[ni][nj] = 1
                now.append((ni, nj))
                dfs_comb(ni, nj)
                visited[ni][nj] = 0
                now.pop()


def powerSet(i, j, n, s, ss):
    if s > C:
        return
    if n == M:
        global temp_ss
        temp_ss = max(temp_ss, ss)
        return
    powerSet(i, j+1, n+1, s+arr[i][j], ss+arr[i][j]**2)
    powerSet(i, j+1, n+1, s, ss)


T = int(input())
for tc in range(1, T+1):
    N, M, C = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 입력 끝

    now = []
    case_list = []
    max_honey = 0
    visited = [[0]*N for _ in range(N)]
    temp_ss = 0
    dfs_comb(0, 0)

    for case in case_list:
        temp_honey = 0
        for i, j in case:
            temp_ss = 0
            powerSet(i, j, 0, 0, 0)
            temp_honey += temp_ss
            max_honey = max(max_honey, temp_honey)
    print('#{} {}'.format(tc, max_honey))

