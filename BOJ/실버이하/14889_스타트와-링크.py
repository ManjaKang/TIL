import itertools

N = int(input())
start_n_link = {i for i in range(N)}
case_list = list(map(set, itertools.combinations(start_n_link, N//2)))
arr = [list(map(int, input().split())) for _ in range(N)]

ans = 1000000
for case in case_list:
    start = case
    link = start_n_link - start
    start_stats = 0
    for i in start:
        for j in start:
            start_stats += arr[i][j]
    link_stats = 0
    for i in link:
        for j in link:
            link_stats += arr[i][j]
    ans = min(ans, abs(start_stats - link_stats))
print(ans)
