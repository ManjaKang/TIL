N, M, V = map(int, input().split())
node_list = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    node_list[a].append(b)
    node_list[b].append(a)
for node in node_list:
    node.sort()
visited = [0] * (N + 1)
visited[V] = 1
stack = [V]
ans_dfs = [V]
while stack:
    now = stack.pop()
    for node in node_list[now]:
        if visited[node] == 0:
            visited[node] = 1
            stack.append(node)
            ans_dfs.append(node)


visited = [0] * (N + 1)
visited[V] = 1
stack = [V]
ans_bfs = [V]
while stack:
    now = stack.pop(0)

    for node in node_list[now]:
        if visited[node] == 0:
            visited[node] = 1
            ans_bfs.append(node)
            stack.append(node)
print(*ans_dfs)
print(*ans_bfs)
