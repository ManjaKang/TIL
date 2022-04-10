import collections


def prim(s):
    visited = [False] * (N+1)
    pi = [1000000] * (N+1)
    pi[s] = 0
    for _ in range(N):
        min_s = 10000000
        min_idx = 0
        for i in range(1, N+1):
            if not visited[i] and min_s > pi[i]:
                min_s = pi[i]
                min_idx = i
        visited[min_idx] = True

        for i in adjacency_dict[min_idx]:
            if not visited[i] and pi[i] > pi[min_idx] + 1:
                pi[i] = min_s + 1
    return pi


N, M = map(int, input().split())
adjacency_dict = collections.defaultdict(list)
for _ in range(M):
    a, b = map(int, input().split())
    adjacency_dict[a].append(b)
    adjacency_dict[b].append(a)

min_s = 10000000
ans = 0
for i in range(1, N+1):
    if min_s > sum(prim(i)):
       ans = i
       min_s = sum((prim(i)))

print(ans)
