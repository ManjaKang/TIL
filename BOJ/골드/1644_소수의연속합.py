def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


N = int(input())
prime_list = []
for i in range(2, N+1):
    if is_prime(i):
        prime_list.append(i)
left = 0
right = 0
_sum = 0
ans = 0
while left < len(prime_list):
    if _sum == N:
        ans += 1
        _sum -= prime_list[left]
        left += 1
    elif _sum < N:
        if right == len(prime_list):
            break
        _sum += prime_list[right]
        right += 1
    else:
        _sum -= prime_list[left]
        left += 1

print(ans)