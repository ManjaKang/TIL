import collections


def fibo(n):
    for i in range(2, n+1):
        dp_cnt[i] = (dp_cnt[i-1][0] + dp_cnt[i-2][0], dp_cnt[i-1][1] + dp_cnt[i-2][1])
    return dp_cnt[n]


T = int(input())
for tc in range(T):
    N = int(input())
    dp_cnt = collections.defaultdict(int)
    dp_cnt[0] = (1, 0)
    dp_cnt[1] = (0, 1)
    ans = fibo(N)
    print(*ans)