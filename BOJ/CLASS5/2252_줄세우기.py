from collections import deque


def sol():
    for i in range(N):
        if in_num[i] == 0:
            que.append(i)
            visited[i] = 1

    while que:
        now = que.popleft()
        ans_list.append(now + 1)
        for a in adj_list[now]:
            in_num[a] -= 1
            if in_num[a] == 0:
                que.append(a)


N, M = map(int, input().split())
adj_list = [[] for _ in range(N)]
in_num = [0] * N
que = deque()
visited = [0] * N
ans_list = []
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    adj_list[a].append(b)
    in_num[b] += 1

sol()
print(*ans_list)
