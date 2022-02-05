for i in range(1, 11):
    N = int(input())
    nums = list(map(int, input().split()))
    nums.append(0)
    nums.append(0)
    nums.insert(0,0)
    nums.insert(0,0)
    res_num = 0
    for j in range(2,N+2):
        ref_list = [nums[j-2], nums[j-1], nums[j+1], nums[j+2]]
        ref_max = max(ref_list)
        if nums[j] < ref_max:
            continue
        res_num += nums[j] - ref_max

    print('#{} {}'.format(i, res_num))