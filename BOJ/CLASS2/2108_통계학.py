import collections
N = int(input())
arr = [int(input()) for _ in range(N)]
cnt_dict = collections.defaultdict(int)
arr.sort()
for a in arr:
    cnt_dict[a] += 1
mode_val = max(cnt_dict.values())
cnt = 0
for key, val in cnt_dict.items():
    if val == mode_val:
        cnt += 1
        mode = key
        if cnt == 2:
            mode = key
            break
print(round(sum(arr)/N))
print(arr[N//2])
print(mode)
print((arr[-1]-arr[0]))
