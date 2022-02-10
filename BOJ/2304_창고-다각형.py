N = int(input())
LH_list = []
highest = 0
last = 0
idx_highest = 0
for i in range(N):
    L, H = map(int, input().split())
    LH_list.append((L, H))
    if last < L:
        last = L
    if highest < H:
        highest = H
        idx_highest = L
arr = [0] * (last + 1)
for l, h in LH_list:
    arr[l] = h

prev_h = 0
for i in range(idx_highest):
    if arr[i] < prev_h:
        arr[i] = prev_h
    else:
        prev_h = arr[i]

prev_h = 0
for i in range(last, idx_highest, -1):
    if arr[i] < prev_h:
        arr[i] = prev_h
    else:
        prev_h = arr[i]
ans = 0
for a in arr:
    ans += a

print(ans)
