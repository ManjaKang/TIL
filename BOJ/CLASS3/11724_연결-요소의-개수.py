import collections


def dfs(n):
    stack.append(n)
    while stack:
        now = stack.pop()
        for v in connect_dict[now]:
            if visited[v] == 0:
                visited[v] = 1
                stack.append(v)


N, M = map(int, input().split())
connect_dict = collections.defaultdict(list)
for _ in range(M):
    a, b = map(int, input().split())
    connect_dict[a].append(b)
    connect_dict[b].append(a)

visited = [0] * (N+1)
stack = []
cnt = 0

for i in range(1, N+1):
    if visited[i] == 0:
        visited[i] = 1
        cnt += 1
        dfs(i)

print(cnt)