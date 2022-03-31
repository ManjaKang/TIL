def dfs():
    cnt = 0
    stack.append(1)
    while stack:
        now = stack.pop()
        visited[now] = 1
        for i in range(N+1):
            if (E_arr[now][i] == 1) and (visited[i] == 0):
                visited[i] = 1
                stack.append(i)
                cnt += 1
    return cnt
# 함수 선언 끝


N = int(input())
E = int(input())
E_arr = [[0]*(N+1) for _ in range(N+1)]
for _ in range(E):
    a, b = map(int, input().split())
    E_arr[a][b] = 1
    E_arr[b][a] = 1
# 입력 끝

stack = []
visited = [0] * (N+1)
# 변수 선언 끝

print(dfs())