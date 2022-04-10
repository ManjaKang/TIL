def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if not n % i:
            return False
    return True


N = int(input())
arr = list(map(int, input().split()))
cnt = 0
for a in arr:
    if is_prime(a):
        cnt += 1
print(cnt)