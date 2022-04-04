dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*101 for _ in range(101)]
max_x = 0
max_y = 0
for x, y, d, r in arr:
    max_x = max(max_x, x)
    max_y = max(max_y, y)
    move = [d]
    for _ in range(r):
        temp = []
        for i in range(len(move)):
            temp.append((move[-1 - i] + 1) % 4)
        move += temp
    visited[x][y] = 1
    for m in move:
        x = x + dx[m]
        y = y + dy[m]
        if (0 <= x <= 100) and (0 <= y <= 100) and (visited[x][y] == 0):
            visited[x][y] = 1
            max_x = max(max_x, x)
            max_y = max(max_y, y)

ans = 0
for i in range(max_x):
    for j in range(max_y):
        if visited[i][j] and visited[i+1][j] and visited[i][j+1] and visited[i+1][j+1]:
            ans += 1
print(ans)