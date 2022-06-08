from collections import defaultdict, deque
import sys
import heapq
input = sys.stdin.readline


N, M = map(int, input().split())
adj_dict = defaultdict(list)
for _ in range(M):
    a, b, c = map(int, input().split())
    adj_dict[a].append((b, c))
    adj_dict[b].append((a, c))
s, e = map(int, input().split())
visited = [0] * (N+1)
que = []
heapq.heappush(que, (-float('inf'), s))
while que:
    prev_limit, now = heapq.heappop(que)
    prev_limit *= -1
    if visited[e] >= prev_limit:
        continue
    for node, limit in adj_dict[now]:
        now_limit = min(limit, prev_limit)
        if visited[node] < now_limit:
            visited[node] = now_limit
            que.append((-now_limit, node))
print(visited[e])