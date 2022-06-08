import sys
import math
input = sys.stdin.readline


def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])
    return parent[a]


def union(a, b):
    a = find(a)
    b = find(b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a


def cal_dist(A, B):
    return math.sqrt((A[0] - B[0])**2 + (A[1] - B[1])**2)


T = int(input())
for tc in range(T):
    N = int(input())
    parent = [i for i in range(N)]
    arr = []
    visited = [0] * N
    for _ in range(N):
        x, y, r = map(int, input().split())
        arr.append(((x, y), r))
    for i in range(N):
        if visited[i]:
            continue
        for j in range(i+1, N):
            if cal_dist(arr[i][0], arr[j][0]) <= arr[i][1] + arr[j][1]:
                visited[j] = 1
                union(i, j)
    ans = 0
    for idx, root in enumerate(parent):
        if idx == root:
            ans += 1
    print(ans)