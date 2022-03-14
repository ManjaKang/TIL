def dfs():
    stack.append(A)
    visited[A] = 0
    while stack:
        now = stack.pop()
        if now == B:
            return visited[now]
        for i in range(N+1):
            if (visited[i] == 0) and (E_arr[now][i] != 0):
                visited[i] = visited[now] + E_arr[now][i]
                stack.append(i)
    return -1
# 함수 선언 끝


N = int(input())
A, B = map(int, input().split())
m = int(input())
arr = [[] for _ in range(N+1)]
E_arr = [[0]*(N+1) for _ in range(N+1)]
for _ in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
# 입력 끝

stack = []
visited = [0] * (N+1)
# 변수 선언 끝
for i in range(N+1):
    for j in arr[i]:
        # 자식들 체크
        E_arr[j][i] = 1
        E_arr[i][j] = 1
        for k in arr[i]:
            # 형제들 체크
            if k != j:
                E_arr[j][k] = 2
# 엣지 리스트 완성

print(dfs())
