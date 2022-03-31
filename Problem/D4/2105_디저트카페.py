import sys
sys.stdin = open('sample_input.txt', 'r')


def dfs(i, j):
    for idx in range(4):
        ni = i + di[idx]
        nj = j + dj[idx]
        if (0 <= ni < N) and (0 <= nj < N) and



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 입력 끝

    di = [1, 1, -1, -1]
    dj = [1, -1, -1, 1]
    visited = [[0] * N for _ in range(N)]
    # 변수 선언 끝