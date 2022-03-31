import sys
sys.stdin = open('sample_input.txt', 'r')


def dfs(n, s):
    if n > 12:
        global ans
        if ans > s:
            ans = s
        return
    dfs(n+1, s+day*arr[n])
    dfs(n+1, s+month)
    dfs(n+3, s+month3)
    dfs(n+12, s+year)


T = int(input())
for tc in range(1, T+1):
    day, month, month3, year = map(int, input().split())
    arr = [0] + list(map(int, input().split()))
    # 입력 끝

    ans = 1000000

    dfs(0, 0)

    print('#{} {}'.format(tc, ans))