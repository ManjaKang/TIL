import heapq
from collections import defaultdict


def dijkstra(start):
    distances = defaultdict(lambda: float('inf'))
    distances[start] = 0
    heap = []
    heapq.heappush(heap, (distances[start], start))
    while heap:
        cur_dist, cur_node = heapq.heappop(heap)
        if distances[cur_node] < cur_dist:
            continue
        for adj_node, dist in adj_dict[cur_node]:
            weigted_dist = cur_dist + dist
            if weigted_dist < distances[adj_node]:
                distances[adj_node] = weigted_dist
                heapq.heappush(heap, (weigted_dist, adj_node))
    return distances


N = int(input())
M = int(input())
adj_dict = defaultdict(list)
for _ in range(M):
    a, b, c = map(int, input().split())
    adj_dict[a].append((b, c))
A, B = map(int, input().split())
distances = dijkstra(A)
print(distances[B])