import heapq
import sys
N = int(input())
heap = []
for _ in range(N):
    a = int(sys.stdin.readline())
    if a != 0:
        heapq.heappush(heap, a)
    else:
        try:
            print(heapq.heappop(heap))
        except:
            print(0)
