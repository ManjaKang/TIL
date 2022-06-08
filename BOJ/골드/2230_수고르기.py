# PyPy 216ms
N, M = map(int, input().split())
arr = [int(input()) for _ in range(N)]
arr.sort()
min_diff = float('inf')
left = 0
right = 1
while left < N and right < N:
    temp = arr[right] - arr[left]
    if temp == M:
        min_diff = M
        break
    elif temp > M:
        left += 1
        min_diff = min(min_diff, temp)
    else:
        right += 1

print(min_diff)