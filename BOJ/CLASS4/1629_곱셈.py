def power(a, b):
    if b == 1:
        return a % C
    if b % 2:
        return power(a, b//2) ** 2 * a % C
    else:
        return power(a, b//2) ** 2 % C


A, B, C = map(int, input().split())
print(power(A, B))
