def numToPoint(n):
    if len(dp) >= n:
        return dp[n]
    else:
        prev = dp[0]
        for i in range(1, n + 1):
            nx = prev[0] + dx
            ny = prev[1] + dy
            if ny <= 0:
                ny = nx
                nx = 1
            prev = (nx, ny)
            dp.append(prev)
        return dp[n]


def pointAdd(a, b):
    return a[0] + b[0], a[1] + b[1]


dp = [(0, 0)]
T = int(input())
for tc in range(1, T + 1):
    p, q = map(int, input().split())
    # 입력 끝

    dx = 1
    dy = -1
    # 변수 선언 끝

    numToPoint(50000)
    num = pointAdd(numToPoint(p), numToPoint(q))
    ans = dp.index(num)

    print('#{} {}'.format(tc, ans))