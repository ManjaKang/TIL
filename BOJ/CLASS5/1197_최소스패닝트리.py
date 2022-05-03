def prim():
    visited = [0] * V
    pri = [1000000] * V
    pri[0] = 0
    for _ in range(V):
        min_d = 1000000
        min_idx = 0
        for i in range(V):
            if visited[i] == 0 and min_d > pri[i]:
                min_idx = i
                min_d = pri[i]
        visited[min_idx] = 1
        for i, w in adj_list[min_idx]:
            if visited[i] == 0 and w < pri[i]:
                pri[i] = w
    return sum(pri)


V, E = map(int, input().split())
adj_list = [[] for _ in range(V)]
for _ in range(E):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    adj_list[a].append((b, c))
    adj_list[b].append((a, c))

print(prim())
