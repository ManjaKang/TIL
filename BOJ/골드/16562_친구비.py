def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])
    return parent[a]


def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        if arr[a] > arr[b]:
            parent[a] = b
        else:
            parent[b] = a


N, M, K = map(int, input().split())
arr = [0] + list(map(int, input().split()))
parent = [i for i in range(N+1)]
for _ in range(M):
    v, w = map(int, input().split())
    union(v, w)
ans = 0
for idx, root in enumerate(parent):
    if idx == root:
        ans += arr[idx]
        if ans > K:
            print('Oh no')
            break
else:
    print(ans)