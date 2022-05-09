def prim():
    visited = [False]*(N+1)
    pi = [1000000] * (N+1)
    pi[arr[1][0][0]] = 0
    for _ in range(N):
        min_d = 1000000
        min_idx = 0
        for i in range(1, N+1):
            if not visited[i] and min_d > pi[i]:
                min_d = pi[i]
                min_idx = i
        visited[min_idx] = True
        for a, val in arr[min_idx]:
            if not visited[a] and pi[a] > val:
                pi[a] = val
    return sum(pi) - 1000000 - min_d


N, M = map(int, input().split())
input_arr = [list(map(int, input().split())) for _ in range(M)]
input_arr.sort(key=lambda x: x[2])
arr = [[] for _ in range(N+1)]
for i in range(M):
    a, b, cost = input_arr[i]
    arr[a].append((b, cost))

print(prim())
