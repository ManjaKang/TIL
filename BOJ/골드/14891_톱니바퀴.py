import collections
# 인덱스와 톱니 번호를 맞추기 위해 arr[0] 추가
arr = [0]
arr.append(collections.deque(list(map(int, input()))))
arr.append(collections.deque(list(map(int, input()))))
arr.append(collections.deque(list(map(int, input()))))
arr.append(collections.deque(list(map(int, input()))))

K = int(input())
rotate_arr = [list(map(int, input().split())) for _ in range(K)]

for gear, di in rotate_arr:
    rotate_list = [(gear, di)]      # 회전할 톱니들을 저장할 리스트
    gear_r = gear + 1
    gear_l = gear - 1

    # 오른쪽 방향 회전하는 톱니 구하기
    gear_prev = gear
    di_prev = di
    while gear_r < 5:
        if arr[gear_prev][2] == arr[gear_r][6]:
            break
        rotate_list.append((gear_r, -di_prev))
        gear_prev = gear_r
        gear_r += 1
        di_prev = -di_prev

    # 왼쪽 방향 회전하는 톱니 구하기
    gear_prev = gear
    di_prev = di
    while gear_l > 0:
        if arr[gear_prev][6] == arr[gear_l][2]:
            break
        rotate_list.append((gear_l, -di_prev))
        gear_prev = gear_l
        gear_l -= 1
        di_prev = -di_prev

    # 톱니들 회전 시키기
    for g, ro in rotate_list:
        arr[g].rotate(ro)

# 점수 구하기
ans = 0
if arr[1][0] == 1:
    ans += 1
if arr[2][0] == 1:
    ans += 2
if arr[3][0] == 1:
    ans += 4
if arr[4][0] == 1:
    ans += 8

print(ans)
