# PyPy 108ms
N, M = map(int, input().split())
arr = list(map(int, input().split()))
left = 0
right = 0
_sum = 0
ans = 0
while left < N:
    if _sum == M:
        ans += 1
        _sum -= arr[left]
        left += 1
    elif _sum < M:
        if right == N:
            break
        _sum += arr[right]
        right += 1
    else:
        _sum -= arr[left]
        left += 1
print(ans)