def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])
    return parent[a]


def union(a, b):
    a = find(a)
    b = find(b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a


N = int(input())
M = int(input())
parent = [i for i in range(N)]
for i in range(N):
    arr = list(map(int, input().split()))
    for j in range(N):
        if arr[j] == 1:
            union(i, j)

arr = list(map(int, input().split()))
parent_set = set()
for a in arr:
    parent_set.add(find(a-1))

if len(parent_set) == 1:
    print('YES')
else:
    print('NO')
