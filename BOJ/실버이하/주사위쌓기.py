def next_dice(a):
    if a == 0:
        b = 5
    if a == 1:
        b = 3
    if a == 2:
        b = 4
    if a == 3:
        b = 1
    if a == 4:
        b = 2
    if a == 5:
        b = 0
    return b


T = int(input())
dices = [0] * T
for tc in range(T):
    dices[tc] = list(map(int, input().split()))
ans = 0
for i in range(6):
    val = 0
    nums = []
    target = dices[0][i]
    for dice in dices:
        k = dice.index(target)
        j = next_dice(k)
        nums.append((dice[k], dice[j]))
        target = dice[j]

    sum_side = 0
    for num in nums:
        if 6 in num and 5 in num:
            sum_side += 4
        elif 6 in num:
            sum_side += 5
        else:
            sum_side += 6
    if ans < sum_side:
        ans = sum_side
print(ans)
