arr = [int(input()) for _ in range(9)]
ans_idx = 0
max_n = 0
for idx, a in enumerate(arr):
    if max_n < a:
        max_n = a
        ans_idx = idx
print(max_n)
print(ans_idx+1)