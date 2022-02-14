def binarySearch(l, target):
    cnt = 1
    i = 1
    c = int((l + i) / 2)
    while c != target:
        if c > target:
            l = c
            c = int((l + i) / 2)
            cnt += 1
        else:
            i = c
            c = int((l + i) / 2)
            cnt += 1
    return cnt


T = int(input())
for tc in range(1, T+1):
    total_page, A, B = map(int, input().split())
    a_cnt = binarySearch(total_page, A)
    b_cnt = binarySearch(total_page, B)
    if a_cnt > b_cnt:
        win = 'B'
    if a_cnt < b_cnt:
        win = 'A'
    if a_cnt == b_cnt:
        win = '0'
    print('#{} {}'.format(tc, win))

