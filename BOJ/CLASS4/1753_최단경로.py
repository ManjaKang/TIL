def dijkstra():
    visited = [0] * V
    di = [1000000] * V
    di[K] = 0
    for _ in range(V):
        min_d = 1000000
        min_idx = 0
        for i in range(V):
            if visited[i] == 0 and min_d > di[i]:
                min_d = di[i]
                min_idx = i
        visited[min_idx] = 1

        for i, dist in arr[min_idx]:
            if visited[i] == 0 and dist + min_d < di[i]:
                di[i] = dist + min_d
    return di


V, E = map(int, input().split())
K = int(input())
K -= 1
arr = [[] for _ in range(V)]
for _ in range(E):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    arr[u].append((v, w))
# 입력 끝
ans = dijkstra()
for a in ans:
    if a == 1000000:
        print('INF')
    else:
        print(a)

