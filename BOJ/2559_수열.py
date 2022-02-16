N, K = map(int, input().split())
temps = list(map(int, input().split()))
arr = []
for i in range(1, N):
    arr.append(temps[i] + arr[-1])
ans = arr[K-1] - arr[0]
for i in range(N-K+1):
    if ans < arr[i + K - 1] - arr[i]:
        ans = arr[i + K - 1] - arr[i]
print(ans)