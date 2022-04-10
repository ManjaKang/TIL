import itertools
N, M = map(int, input().split())
arr = [i for i in range(1, N+1)]
case_list = list(itertools.combinations_with_replacement(arr, M))
for case in case_list:
    print(*case)