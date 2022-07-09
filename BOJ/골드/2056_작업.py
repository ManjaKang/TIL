from collections import deque

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
adj_list = [[] for _ in range(N+1)]
indegree_list = [0] * (N+1)
ans = arr[0][0]
que = deque()
time_list = [0] + [arr[i][0] for i in range(N)]
for i in range(1, N):
    for a in arr[i][2:]:
        adj_list[a].append(i+1)
        indegree_list[i+1] += 1

for i in range(1, N+1):
    if indegree_list[i] == 0:
        que.append(i)

while que:
    now = que.popleft()
    for a in adj_list[now]:
        indegree_list[a] -= 1
        if indegree_list[a] == 0:
            que.append(a)
            temp = 0
            for b in arr[a-1][2:]:
                temp = max(temp, time_list[b])
            time_list[a] += temp

print(max(time_list))