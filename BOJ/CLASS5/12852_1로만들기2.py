def bfs(i, arr):
    if i == 1:
        print(arr)
        return
    if i % 3 == 0 and visited[i]+1 < visited[i//3]:
        bfs(i//3, arr+[i//3])
    if i % 2 == 0 and visited[i]+1 < visited[i//2]:
        bfs(i//2, arr+[i//2])
    if visited[i]+1 < visited[i-1]:
        bfs(i-1, arr+[i-1])


N = int(input())
visited = [1000000]*(N+1)
visited[N] = 0
bfs(N, [N])