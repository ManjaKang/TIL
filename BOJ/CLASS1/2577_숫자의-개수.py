arr = [int(input()) for _ in range(3)]
m = 1
for a in arr:
    m *= a
cnt_list = [0] * 10
for ch in str(m):
    cnt_list[int(ch)] += 1
for cnt in cnt_list:
    print(cnt)