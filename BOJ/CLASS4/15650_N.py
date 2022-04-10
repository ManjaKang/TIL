import itertools


N, M = map(int, input().split())
arr = [i for i in range(1, N+1)]
ans = list(itertools.combinations(arr, M))

for a in ans:
    print(*a)