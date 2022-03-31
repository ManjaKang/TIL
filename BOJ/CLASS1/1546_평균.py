N = int(input())
arr = list(map(int, input().split()))
m = max(arr)
ans = 0
for a in arr:
    ans += a / m * 100
print(ans/N)
