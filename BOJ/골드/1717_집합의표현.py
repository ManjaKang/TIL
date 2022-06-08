# PyPy 5028ms
import sys
sys.setrecursionlimit(10**5)


def find_parent(a):
    if parent[a] != a:
        parent[a] = find_parent(parent[a])
    return parent[a]


def union(a, b):
    a_p = find_parent(a)
    b_p = find_parent(b)
    if a_p < b_p:
        parent[b_p] = a_p
    else:
        parent[a_p] = b_p


N, M = map(int, input().split())
parent = [i for i in range(N + 1)]
for _ in range(M):
    flag, a, b = map(int, input().split())
    if flag:
        if find_parent(a) == find_parent(b):
            print('YES')
        else:
            print('NO')
    else:
        union(a, b)
