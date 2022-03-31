dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
x, y = 1, 1
C, R = map(int, input().split())
K = int(input())
idx = 1
delta = 0
stack = [(x, y)]
while idx < K:
    nx = x + dx[delta]
    ny = y + dy[delta]
    if (nx == C) or (ny == R) or (x == 1) or (y == 0) or (x, y) in stack:
        delta = (delta + 1) % 4
    x = x + dx[delta]
    y = y + dy[delta]
    stack.append((x, y))
    idx += 1
    print(stack)
print(x, y)