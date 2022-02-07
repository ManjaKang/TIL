T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    nums = list(map(int, input()))
    num_list = []
    count_list = []
    nums.sort(reverse=True)
    temp = -1
    for num in nums:
        if temp != num:
            temp = num
            num_list.append(num)
            count_list.append(nums.count(num))
    max_count = max(count_list)
    idx = count_list.index(max_count)
    max_num = num_list[idx]
    print('#{} {} {}'.format(test_case, max_num, max_count))

    