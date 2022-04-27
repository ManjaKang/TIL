import sys
sys.stdin = open('test.txt', 'r')
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(2)]
    for j in range(1, N):
        if j == 1:
            arr[1][1] += arr[0][0]
            arr[0][1] += arr[1][0]
        else:
            arr[0][j] += max(arr[1][j-1], arr[1][j-2])
            arr[1][j] += max(arr[0][j-1], arr[0][j-2])
    print(max(arr[0][-1], arr[1][-1]))