import math


def cal_dist(a, b):
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)


def prim():
    visited = [False]*N
    pi = [1000000]*N
    pi[0] = 0
    for _ in range(N):
        min_d = 1000000
        min_idx = 0
        for i in range(N):
            if not visited[i] and min_d > pi[i]:
                min_d = pi[i]
                min_idx = i
        visited[min_idx] = True
        for i in range(N):
            if not visited[i] and dist_arr[min_idx][i] != 0 and dist_arr[min_idx][i] < pi[i]:
                pi[i] = dist_arr[min_idx][i]
    return sum(pi)


N = int(input())
arr = [list(map(float, input().split())) for _ in range(N)]
dist_arr = [[8]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        dist_arr[i][j] = cal_dist(arr[i], arr[j])

print(prim())