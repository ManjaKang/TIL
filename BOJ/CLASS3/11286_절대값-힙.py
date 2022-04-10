import sys
import heapq

N = int(input())
heap = []
for _ in range(N):
    a = int(sys.stdin.readline())
    if a != 0:
        heapq.heappush(heap, (abs(a), a))
    else:
        try:
            print(heapq.heappop(heap)[1])
        except:
            print(0)