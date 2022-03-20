def calDistance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def dfs():
    while stack:
        now = stack.pop()
        for idx, a in enumerate(arr):
            if (visited[idx] == 0) and calDistance(now, a) <= 1000:
                visited[idx] = 1
                stack.append(a)
    if visited[-1] == 1:
        return 'happy'
    else:
        return 'sad'


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n+2)]
    # 입력 끝

    stack = [arr[0]]
    visited = [0] * (n+2)
    visited[0] = 1
    # 변수 선언 끝

    ans = dfs()
    print(ans)
