def calDirector(n):
    cnt = 1
    people = arr[n] - B
    if people <= 0:
        return cnt
    cnt += people // C
    if people % C != 0:
        cnt += 1
    return cnt


N = int(input())
arr = list(map(int, input().split()))
B, C = map(int, input().split())
ans = 0
for i in range(N):
    ans += calDirector(i)
print(ans)