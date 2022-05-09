def count_one(num):
    cnt = 0
    while num > 0:
        num = num & num - 1
        cnt += 1
    return cnt


def count_one2(num):
    if num <= 1:
        return num
    else:
        return count_one2(num/2) + num / 2


# A, B = map(int, input().split())

ans = 0
for i in range(1, 10):
    ans += count_one(i)
print(ans)
print(count_one2(10))