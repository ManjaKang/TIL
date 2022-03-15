import sys
sys.stdin = open('sample_input.txt', 'r')


# 몬스터와, 고객들의 순열을 생성하는 함수
def perm_dfs():
    if len(now) == R:
        case_list.append(now[:])
        return
    for i in range(R):
        if visited[i] == 0:
            # 고객이 몬스터보다 먼저 등장하면
            # 추가하지 않음
            if (target_list[i] < 0) and (-target_list[i] not in now):
                continue
            now.append(target_list[i])
            visited[i] = 1
            perm_dfs()
            now.pop()
            visited[i] = 0
    return


# 두 점사이의 이동거리를 구하는 함수
def cal_len(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])
# 함수 선언 끝


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 입력 끝

    target_list = []
    point_list = []
    monster_list = [0] * 5
    now = []
    case_list = []
    ans_list = []
    min_sum = 1000
    # 변수 선언 끝

    for i in range(N):
        for j in range(N):
            if arr[i][j] != 0:
                target_list.append(arr[i][j])
                point_list.append((i, j))
    for target in target_list:
        if target > 0:
            monster_list[target] = 1
    R = len(target_list)
    visited = [0] * R
    H = R // 2
    # 변수 입력 끝

    perm_dfs()
    # 경우의 수 생성 완료

    for case in case_list:
        prev = (0, 0)
        temp_sum = 0
        for c in case:
            # 현재 타겟으로 삼은 위치를 point 저장
            point = point_list[target_list.index(c)]
            temp_sum += cal_len(prev, point)
            prev = point
        if min_sum > temp_sum:
            min_sum = temp_sum
    print('#{} {}'.format(tc, min_sum))
