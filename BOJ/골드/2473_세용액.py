N = int(input())
arr = list(map(int, input().split()))
arr.sort()
min_val = float('inf')
for a in arr:
    left = 0
    right = N - 1
    while left < right:
        if a == arr[left]:
            left += 1
            continue
        if a == arr[right]:
            right -= 1
            continue
        _sum = arr[left] + arr[right] + a
        if min_val > abs(_sum):
            min_val = abs(_sum)
            ans = [a, arr[left], arr[right]]

        if _sum < 0:
            left += 1
        elif _sum > 0:
            right -= 1
        else:
            break
ans.sort()
print(*ans)