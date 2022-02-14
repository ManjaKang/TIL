N = int(input())
nums = list(map(int, input().split()))
max_increase = 0
max_decrease = 0
cnt_increase = 1
cnt_decrease = 1
for i in range(0, N-1):
    if nums[i] < nums[i+1]:
        cnt_increase += 1
        if max_decrease < cnt_decrease:
            max_decrease = cnt_decrease
        cnt_decrease = 1
    elif nums[i] > nums[i+1]:
        cnt_decrease += 1
        if max_increase < cnt_increase:
            max_increase = cnt_increase
        cnt_increase = 1
    else:
        cnt_increase += 1
        cnt_decrease += 1
        if max_decrease < cnt_decrease:
            max_decrease = cnt_decrease
        if max_increase < cnt_increase:
            max_increase = cnt_increase

ans = max_increase if max_decrease < max_increase else max_decrease
print(ans)