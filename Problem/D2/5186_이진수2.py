import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    num = float(input())
    ans = ''
    for i in range(1, 13):
        a = 2 ** (-i)
        if num >= a:
            ans += '1'
            num -= a
        else:
            ans += '0'
        if num == 0:
            break
    else:
        ans = 'overflow'

    print('#{} {}'.format(tc, ans))
