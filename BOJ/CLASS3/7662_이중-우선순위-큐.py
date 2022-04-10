import heapq
T = int(input())
for tc in range(T):
    k = int(input())
    heap = []
    for _ in range(k):
        oper, num = input().split()
        num = int(num)
        if oper == 'I':
            heapq.heappush(heap, num)
        else:
            if heap:
                if num == 1:
                    heap.remove(max(heap))
                else:
                    heapq.heappop(heap)
    if heap:
        print(max(heap), heap[0])
    else:
        print('EMPTY')
