import itertools

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
case_list = list(itertools.permutations(arr, M))
for case in case_list:
    print(*case)
