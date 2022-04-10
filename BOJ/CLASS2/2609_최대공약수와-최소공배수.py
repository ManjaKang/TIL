import heapq

a, b = map(int, input().split())
heap = []
heapq.heappush(heap, a)
heapq.heappush(heap, b)
while heap[0] != 0:
    c = heapq.heappop(heap)
    d = heapq.heappop(heap)
    heapq.heappush(heap, d % c)
    heapq.heappush(heap, c)
heapq.heappop(heap)
print(heap[0])
print(a*b//heap[0])