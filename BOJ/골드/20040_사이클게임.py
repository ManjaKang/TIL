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
        return True
    elif a < b:
        parent[b] = a
        return True
    else:
        return False


N, M = map(int, input().split())
parent = [i for i in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    if union(a, b):
        continue
    else:
        print(i+1)
        break
else:
    print(0)
