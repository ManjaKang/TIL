import sys

sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N, num = input().split()
    N = int(N)
    num = int(num, 16)
    ans = ''
    for i in range(4 * N):
        ans += str(num%2)
        num = num >> 1
    ans = ans[::-1]
    print('#{} {}'.format(tc, ans))
