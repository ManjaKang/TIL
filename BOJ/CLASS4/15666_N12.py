import itertools
N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
case_list = list(itertools.combinations_with_replacement(arr, M))
case_list = list(set(case_list))
case_list.sort()
for case in case_list:
    print(*case)