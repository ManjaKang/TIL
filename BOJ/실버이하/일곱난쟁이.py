def isInCase(c):
    cnt = 0
    while c > 0:
        c &= c - 1
        cnt += 1
    if cnt == 7:
        return True
    else:
        return False


arr = []
cases = []
for _ in range(9):
    arr.append(int(input()))

nums = [n for n in range(0b001111111, 0b111111101)]

for num in nums:
    if isInCase(num):
        cases.append(num)

ans_case = 0
for case in cases:
    height = 0
    idx = 0
    temp_case = case
    while case > 0:
        if case % 2 == 1:
            height += arr[idx]
        idx += 1
        case = case >> 1
    if height == 100:
        ans_case = temp_case
        break

ans_list = []
idx = 0
while ans_case > 0:
    if ans_case % 2 == 1:
        ans_list.append(arr[idx])
    idx += 1
    ans_case = ans_case // 2

for i in range(len(ans_list) - 1, 0, -1):
    for j in range(i):
        if ans_list[j] > ans_list[j + 1]:
            ans_list[j], ans_list[j + 1] = ans_list[j + 1], ans_list[j]
for ans in ans_list:
    print(ans)
