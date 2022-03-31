import sys
sys.stdin = open('sample_input.txt', 'r')


def game(p: list):
    i, j, c = p[:]
    di = [0, 1, 0, -1, 1, 1, -1, -1]
    dj = [1, 0, -1, 0, 1, -1, 1, -1]
    board_arr[i][j] = c
    for idx in range(8):
        temp_list = []
        for k in range(1, N):
            ni = i + di[idx] * k
            nj = j + dj[idx] * k
            if not (0 <= ni < N and 0 <= nj < N):
                break
            if board_arr[ni][nj] != 0 and board_arr[ni][nj] != c:
                temp_list.append((ni, nj))
                continue
            if board_arr[ni][nj] == c:
                for i, j in temp_list:
                    board_arr[i][j] = c


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    p_list = []
    for _ in range(M):
        pi, pj, pc = map(int, input().split())
        p_list.append((pi-1, pj-1, pc))
    # 입력 끝

    board_arr = [[0] * N for _ in range(N)]
    board_arr[N // 2][N // 2] = 2
    board_arr[N // 2 - 1][N // 2 - 1] = 2
    board_arr[N // 2 - 1][N // 2] = 1
    board_arr[N // 2][N // 2 - 1] = 1
    # 초기 보드 생성 끝

    for p in p_list:
        game(p)

    cnt1 = 0
    cnt2 = 0
    for board_row in board_arr:
        cnt1 += board_row.count(1)
        cnt2 += board_row.count(2)
    print('#{} {} {}'.format(tc, cnt1, board_arr))
