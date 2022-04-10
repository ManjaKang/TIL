def dfs(n, p, m, pr, di, s):
    # 종료 조건
    if n == N:
        global min_s, max_s
        min_s = min(min_s, s)
        max_s = max(max_s, s)
        return
    # 재귀 호출 부분
    if p:
        dfs(n+1, p-1, m, pr, di, s+arr[n])
    if m:
        dfs(n+1, p, m-1, pr, di, s-arr[n])
    if pr:
        dfs(n+1, p, m, pr-1, di, s*arr[n])
    if di:
        dfs(n+1, p, m, pr, di-1, int(s/arr[n]))


N = int(input())
arr = list(map(int, input().split()))
plus, minus, product, div = map(int, input().split())
min_s = 1000000000
max_s = -1000000000

dfs(1, plus, minus, product, div, arr[0])

print(max_s)
print(min_s)