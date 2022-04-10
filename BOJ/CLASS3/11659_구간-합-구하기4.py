import sys
N, M = map(int, input().split())
arr = list(map(int, input().split()))
for i in range(1, N):
    arr[i] += arr[i-1]
arr.insert(0, 0)
for _ in range(M):
    s, e = map(int, sys.stdin.readline().split())
    s -= 1
    print(arr[e] - arr[s])