import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**4)


def find(a):
    if air_port[a] != a:
        air_port[a] = find(air_port[a])
    return air_port[a]


def union(a, b):
    a = find(a)
    b = find(b)
    if a > b:
        air_port[a] = b
    else:
        air_port[b] = a


G = int(input())
P = int(input())
air_port = {i: i for i in range(G+1)}
ans = 0
for _ in range(P):
    g = int(input())
    g = find(g)
    if g == 0:
        break
    union(g, g-1)
    ans += 1
print(ans)
