ans1 = [0] * 21
ans2 = [0] * 21
ans3 = [0] * 21


def sequence(num_str):
    rlt = ''
    for num in num_str:
        if num == '1':
            rlt += '132'
        if num == '2':
            rlt += '211'
        if num == '3':
            rlt += '232'
    return rlt


def sequence1(n):
    if n == 1:
        return '131'
    if ans1[n] != 0:
        return ans1[n]
    ans1[n] = sequence(sequence1(n-1))
    return ans1[n]


def sequence2(n):
    if n == 1:
        return '211'
    if ans2[n] != 0:
        return ans2[n]
    ans2[n] = sequence(sequence2(n-1))
    return ans2[n]


def sequence3(n):
    if n == 1:
        return '232'
    if ans3[n] != 0:
        return ans3[n]
    ans3[n] = sequence(sequence3(n-1))
    return ans3[n]


num = int(input())
L = int(input())
R = int(input())
N = int(input())

rlt_str = ''
if num == 1:
    rlt_str = sequence1(N)
if num == 2:
    rlt_str = sequence2(N)
if num == 3:
    rlt_str = sequence3(N)

cnt1 = 0
cnt2 = 0
cnt3 = 0
for i in range(L, R+1):
    if rlt_str[i] == '1':
        cnt1 += 1
    if rlt_str[i] == '2':
        cnt2 += 1
    if rlt_str[i] == '3':
        cnt3 += 1

print(cnt1, cnt2, cnt3)