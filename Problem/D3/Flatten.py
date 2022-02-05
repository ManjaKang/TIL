for i in range(1, 11):
    N = int(input())
    nums = list(map(int, input().split()))
    for j in range(N):
        nums[nums.index(max(nums))] -= 1
        nums[nums.index(min(nums))] += 1
    print('#{} {}'.format(i, max(nums) - min(nums)))