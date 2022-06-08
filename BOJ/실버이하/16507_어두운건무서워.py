# PyPy 472ms
import sys
input = sys.stdin.readline
R, C, Q = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]
arr_sum = [[0] * (C + 1) for _ in range(R)]
for i in range(R):
    for j in range(C):
        arr_sum[i][j + 1] = arr_sum[i][j] + arr[i][j]
for _ in range(Q):
    r1, c1, r2, c2 = map(int, input().split())
    s = 0
    for i in range(r1-1, r2):
        s += arr_sum[i][c2] - arr_sum[i][c1 - 1]
    print(s // ((r2 - r1 + 1) * (c2 - c1 + 1)))
