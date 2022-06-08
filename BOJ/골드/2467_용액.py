N = int(input())
arr = list(map(int, input().split()))
ans = []
min_val = float('inf')
left = 0
right = N - 1
while left < right:
    _sum = arr[left] + arr[right]
    if min_val > abs(_sum):
        min_val = abs(_sum)
        ans = [arr[left], arr[right]]

    if _sum > 0:
        right -= 1
    elif _sum < 0:
        left += 1
    else:
        break
print(*ans)