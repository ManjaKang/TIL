N = int(input())
nums = list(map(int, input().split()))
max_num = 0
sum_num = 0
for num in nums:
    if max_num < num:
        max_num = num
    sum_num += num
avr_num = sum_num / N
ans = avr_num / max_num * 100
print(ans)
