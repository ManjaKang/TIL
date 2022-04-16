import sys
sys.stdin = open('sample_input.txt', 'r')


def dfs(p, m, c, d, n, s):
    # 종료 조건
    if n == N:
        global min_s, max_s
        min_s = min(min_s, s)
        max_s = max(max_s, s)
        return

    if p:
        dfs(p-1, m, c, d, n+1, s+arr[n])
    if m:
        dfs(p, m-1, c, d, n+1, s-arr[n])
    if c:
        dfs(p, m, c-1, d, n+1, s*arr[n])
    if d:
        dfs(p, m, c, d-1, n+1, int(s/arr[n]))


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    plus, minus, cross, div = map(int, input().split())
    arr = list(map(int, input().split()))
    min_s = float('inf')
    max_s = -float('inf')
    dfs(plus, minus, cross, div, 1, arr[0])
    print('#{} {}'.format(tc, max_s-min_s))
