N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

dp_r = [0] * N
dp_g = [0] * N
dp_b = [0] * N
dp_r[0] = arr[0][0]
dp_g[0] = arr[0][1]
dp_b[0] = arr[0][2]
for i in range(1, N):
    for j in range(3):
        dp_r[i] = min(dp_g[i-1], dp_b[i-1]) + arr[i][0]
        dp_g[i] = min(dp_r[i-1], dp_b[i-1]) + arr[i][1]
        dp_b[i] = min(dp_g[i-1], dp_r[i-1]) + arr[i][2]

ans = min(dp_r[N-1], dp_g[N-1], dp_b[N-1])
print(ans)
