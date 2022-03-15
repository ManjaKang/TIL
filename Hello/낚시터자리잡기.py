import sys
sys.stdin = open('sample_input2.txt', 'r')


# 3P3 순열을 구하는 함수
def perm():
    if len(now) == 3:
        case_list.append(now[:])
        return
    for i in range(3):
        if visited[i] == 0:
            visited[i] = 1
            now.append(i)
            perm()
            visited[i] = 0
            now.pop()
    return


# 사람들을 입장시키는 함수
# i = 이미 입장한 게이트  수 i == 3이면 sum_list에 지금까지 사람들이 이동한 거리를 더함
# 재귀적으로 호출됨
# ca는 입장하는 순서
# ca =[0, 2, 1] 이면 0번 2번 1번 게이트 순으로 입장함
# 만약 입장할 사람이 한명 남았는데 갈 수 있는 경우가 두가지라면
# 두 경우 모두 재귀적으로 호출함
def go(i, arr, ca):
    global temp_sum
    if i == 3:
        sum_list.append(temp_sum)
        return

    gate = P_list[ca[i]]
    people = N_list[ca[i]]
    distance = 0
    arr = arr[:]
    while people > 0:
        flag_l = False
        flag_r = False
        flag_one = False
        # 마지막 한사람이 남았다면
        # 두가지 경우가 생길 수 있으므로 표시
        if people == 1:
            flag_one = True
        for idx in range(distance, N):
            nl = gate - idx
            nr = gate + idx
            if (0 <= nl < N) and (arr[nl] == 0):
                flag_l = True
            if (0 <= nr < N) and (arr[nr] == 0):
                flag_r = True
            # 좌 우 모두 자리가 남아 있고 사람이 한 사람 남았다면
            # 두 경우 모두 호출
            if flag_l and flag_r and flag_one:
                arr_l = arr[:]
                arr_r = arr[:]
                distance = idx
                temp_sum += distance+1
                arr_r[nr] = distance+1
                arr_l[nl] = distance+1
                go(i+1, arr_r, ca)
                go(i+1, arr_l, ca)
                return

            if flag_l:
                distance = idx
                temp_sum += distance + 1
                arr[nl] = distance+1
                people -= 1
                break
            if flag_r:
                distance = idx
                temp_sum += distance + 1
                arr[nr] = distance+1
                people -= 1
                break
    go(i+1, arr[:], ca)
    return
# 함수 선언 끝


now = []
case_list = []
visited = [0] * 3
perm()
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    G1, N1 = map(int, input().split())
    G2, N2 = map(int, input().split())
    G3, N3 = map(int, input().split())
    P_list = [G1-1, G2-1, G3-1]
    N_list = [N1, N2, N3]
    # 입력 끝

    fish_list = [0] * N
    stack = []
    temp_sum = 0
    sum_list = []
    # 변수 선언 끝

    for case in case_list:
        temp_sum = 0
        go(0, fish_list, case)

    ans = min(sum_list)
    print('#{} {}'.format(tc, ans))
