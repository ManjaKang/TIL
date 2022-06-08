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
parent = [i for i in range(N+1)]
for _ in range(N-2):
    a, b = map(int, input().split())
    union(a, b)


flag = True
ans = []
for idx, root in enumerate(parent):
    if flag:
        flag = False
        continue
    if idx == root:
        ans.append(idx)
print(*ans)