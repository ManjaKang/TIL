N = int(input())
arr = [int(input()) for _ in range(N)]
# 입력 끝

stack = []
ans = []
for i in range(1, N+1):
    stack.append(i)
    ans.append('+')
    while stack and arr and stack[-1] == arr[0]:
        stack.pop()
        arr.pop(0)
        ans.append('-')

if arr:
    print('NO')
else:
    print(*ans, sep='\n')