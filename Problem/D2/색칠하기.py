def coloring(nums):
    temp = [0]*10
    x1,y1,x2,y2 = nums[0:4]
    for i in range(y1, y2+1):
        for j in range(x1, x2+1):
            temp[i] += 1<<j
    return temp

def countOne(bi):
    cnt = 0
    while bi > 0:
        bi = bi & bi-1
        cnt += 1
    return cnt

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nums = [0]*N
    reds = [0]*10
    blues = [0]*10
    for i in range(N):
        nums[i] = list(map(int, input().split()))
        temp_li = coloring(nums[i])
        if nums[i][4] == 1:
            for j in range(10):
                reds |= temp_li
        if nums[i][4] == 2:
            for j in range(10):
                blues |= temp_li
    cnt = 0
    for i in range(10):
        cnt += countOne(reds[i] & blues[i])
    print('#{} {}'.format(tc, cnt))

