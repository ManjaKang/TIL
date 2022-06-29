N, K = map(int, input().split())
arr = [[2]*(N+2)] + [[2] + list(map(int, input().split())) + [2] for _ in range(N)] + [[2] * (N+2)]
print(arr)
stack = []
dr = [0, 0, 0, -1, 1]
dc = [0, 1, -1, 0, 0]
for i in range(K):
    r, c, d = map(int, input().split())
    stack.append((i, i, r, c, d))

while stack:
    idx_bottom, idx_top, r, c, di = stack.pop()
    nr = r + dr[di]
    nc = c + dc[di]
    i

print(stack)