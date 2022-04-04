M, N = map(int, input().split())
primes = []
ans = []
for i in range(2, N+1):
    for p in primes:
        if i % p == 0:
            break
    else:
        primes.append(i)
        if M <= i <= N:
            ans.append(i)
print(*ans, sep='\n')