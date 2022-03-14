import sys
sys.stdin = open('sample_input.txt', 'r')


def my_abs(a, b):
    if a-b >= 0:
        return a-b
    return b-a


def comb_dfs(s):
    if len(now) == R:
        case_list.append(now[:])
        return
    for i in range(s, N):
        if visited[i] == 0:
            visited[i] = 1
            now.append(i)
            comb_dfs(i+1)
            visited[i] = 0
            now.pop()
    return
# 함수 선언 끝


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 입력 끝

    R = N // 2
    case_list = []
    now = []
    visited = [0] * N
    min_sub = 1000000
    # 변수 선언 끝

    comb_dfs(0)
    for case1 in case_list:
        temp_sum1 = 0
        temp_sum2 = 0
        temp_sub = 0
        case2 = []
        for i in range(N):
            if i not in case1:
                case2.append(i)

        for i in case1:
            for j in case1:
                temp_sum1 += arr[i][j]
        for i in case2:
            for j in case2:
                temp_sum2 += arr[i][j]
        temp_sub = my_abs(temp_sum1, temp_sum2)
        if min_sub > temp_sub:
            min_sub = temp_sub
    print('#{} {}'.format(tc, min_sub))