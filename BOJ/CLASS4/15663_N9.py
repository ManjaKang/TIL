import itertools
N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
case_list = list(itertools.permutations(arr, M))
case_list = set(case_list)

for case in case_list:
    print(*case)