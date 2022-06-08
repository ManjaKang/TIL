import sys
input = sys.stdin.readline


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


N, M = map(int, input().split())
que = []
ans = 0
last_c = 0
parent = [i for i in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    que.append((c, a, b))

que.sort(reverse=True)
while que:
    c, a, b = que.pop()
    if find(a) != find(b):
        union(a, b)
        ans += c
        last_c = c
print(ans-last_c)
