import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
arr_sum = [0] * (N+1)
for i in range(N):
    arr_sum[i+1] = arr_sum[i] + arr[i]
M = int(input())
for _ in range(M):
    a, b = map(int, input().split())
    print(arr_sum[b]-arr_sum[a-1])