def deleteNum(arr, n):
    temp = n
    while n > 0:
        temp += n % 10
        n //= 10
    return arr.add(temp)


nums = set(range(1, 10001))
nums_sub = set()
for i in range(1, 10001):
    deleteNum(nums_sub, i)
ans = list(nums - nums_sub)
ans.sort()
print(*ans, sep='\n')
