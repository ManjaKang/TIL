# PyPy 296ms
arr = list(input())
bomb = list(input())

stack = arr[:len(bomb)]

if stack == bomb:
    stack = []
for i in range(len(bomb), len(arr)):
    stack.append(arr[i])
    if stack[-len(bomb):] == bomb:
        for _ in range(len(bomb)):
            stack.pop()

ans = ''.join(stack)
if ans == '':
    ans = 'FRULA'
print(ans)