N, S = map(int, input().split())
arr = list(map(int, input().split()))

summary = 0
end = 0
ans = 10000000
for start in range(N):
    while summary < S and end < N:
        summary += arr[end]
        end += 1

    if summary >= S:
        ans = min(ans, end-start)

    summary -= arr[start]

if ans == 10000000:
    ans = 0
print(ans)