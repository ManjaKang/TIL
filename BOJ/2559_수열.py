N, K = map(int, input().split())
temps = list(map(int, input().split()))
ans = -1000000
for i in range(N-K+1):
    sum_total = 0
    for j in range(i, i+K):
        sum_total += temps[j]
    if ans < sum_total:
        ans = sum_total
print(ans)
