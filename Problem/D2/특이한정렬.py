T = int(input())
for tc in range(T):
    N = int(input())
    nums = list(map(int, input().split()))
    temp = []

    for j in range(0, N, 2):
        max_num = nums[j]
        min_num = nums[j]
        max_idx = j
        min_idx = j
        for i in range(j, N):
            if max_num < nums[i]:
                max_num = nums[i]
                max_idx = i
            if min_num > nums[i]:
                min_num = nums[i]
                min_idx = i
        nums[j], nums[max_idx] = nums[max_idx], nums[j]
        nums[j+1], nums[min_idx] = nums[min_idx], nums[j+1]
    print(nums)