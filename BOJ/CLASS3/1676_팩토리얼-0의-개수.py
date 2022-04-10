import math

N = int(input())
n_p = math.factorial(N)
cnt = 0
while n_p > 0:
    if n_p % 10 != 0:
        break
    cnt += 1
    n_p //= 10
print(cnt)