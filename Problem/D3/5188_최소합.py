import sys
sys.stdin = open('sample_input.txt', 'r')


def dfs(i, j):
    global temp_sum, ans
    if temp_sum > ans:
        return
    if (i == N-1) and (j == N-1):
        ans = temp_sum
    for d in range(2):
        ni = i + di[d]
        nj = j + dj[d]
        if (nj < N) and (ni < N):
            temp_sum += arr[ni][nj]
            dfs(ni, nj)
            temp_sum -= arr[ni][nj]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 입력 끝

    di = [0, 1]
    dj = [1, 0]
    ans = 1000000
    temp_sum = arr[0][0]
    dfs(0, 0)

    print('#{} {}'.format(tc, ans))