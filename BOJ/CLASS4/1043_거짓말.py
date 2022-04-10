import collections
N, M = map(int, input().split())
arr_know = list(map(int, input().split()))
true = arr_know[1:]
adj_dict = collections.defaultdict(set)
for i in range(M):
    arr = list(map(int, input().split()))
    for a in arr[1:]:
        adj_dict[a].union(set(arr[1:]))
        print(set(arr[1:]))
print(adj_dict)