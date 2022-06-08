from collections import defaultdict
import heapq





N, M = map(int, input().split())
adj_dict = defaultdict(list)
for _ in range(M):
    a, b, c = map(int, input().split())
    adj_dict[a].append((b, c))
    adj_dict[b].append((a, c))
print(prim())