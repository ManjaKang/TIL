def coloring(nums):
    temp = [0] * 100
    x1, y1, x2, y2 = nums[0:4]
    for i in range(x1, x2):
        for j in range(y1, y2):
            temp[i] += 1 << j
    return temp


def area(nums):
    cnt = 0
    for num in nums:
        while num > 0:
            cnt += 1
            num = num & (num-1)
    return cnt



arr = []
for _ in range(4):
    arr.append(list(map(int, input().split())))
ans_arr = [0] * 100
temp = [0] * 100
for i in range(4):
    temp = coloring(arr[i])
    for j in range(100):
        ans_arr[j] |= temp[j]
print(area(ans_arr))
