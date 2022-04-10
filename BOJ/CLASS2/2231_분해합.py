def decompo_sum(n):
    ans = n
    while n > 0:
        ans += n % 10
        n //= 10
    return ans

N = int(input())
for i in range(1, N):
    if decompo_sum(i) == N:
        print(i)
        break
else:
    print(0)