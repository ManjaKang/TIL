import collections

que = collections.deque()
N = int(input())
arr = [i for i in range(1, N+1)]
que.extend(arr)

while len(que) > 1:
    que.popleft()
    que.rotate(-1)
print(que[0])