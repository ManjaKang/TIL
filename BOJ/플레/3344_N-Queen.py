# 2806_N-Queen 풀이
# 2022-03-31
import sys
sys.stdin = open('sample_input.txt', 'r')


def dfs(i, j):
    global cnt
    # 대각선 값 인덱스
    x1 = i - j + N - 1
    x2 = i + j
    # 가지치기
    if 1 in [arr_r[i], arr_c[j], arr_x1[x1], arr_x2[x2]]:
        return
    # 종료 조건
    if i == N-1:
        cnt += 1
        return
    # 퀸 두기
    arr_r[i] = 1
    arr_c[j] = 1
    arr_x1[x1] = 1
    arr_x2[x2] = 1
    for nj in range(N):
        ans.append(nj)
        dfs(i+1, nj)
    # 백트래킹 된 상황이므로
    # 퀸 둔 것 취소
    arr_r[i] = 0
    arr_c[j] = 0
    arr_x1[x1] = 0
    arr_x2[x2] = 0


N = int(input())
# 입력 끝
cnt = 0
arr_r = [0]*N
arr_c = [0]*N
arr_x1 = [0] * (N*2 - 1)
arr_x2 = [0] * (N*2 - 1)
ans = []
for i in range(N):
    dfs(0, i)
print('#{} {}'.format(tc, cnt))
