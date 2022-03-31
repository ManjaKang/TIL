def dummy():
    ni, nj = 0, 0
    cnt = 0
    direction = 0
    rear = [(0, 0)]
    while True:
        if L_list:
            if L_list[-1] == cnt:
                L_list.pop()
                now_d = D_list.pop()
                if now_d == 'D':
                    direction = (direction + 1) % 4
                elif now_d == 'L':
                    direction = (direction + 3) % 4

        ni += di[direction]
        nj += dj[direction]
        if (0 <= ni < N) and (0 <= nj < N):
            rear.append((ni, nj))
            if arr[ni][nj] == 4:
                arr[ni][nj] = 1
            elif arr[ni][nj] == 1:
                return cnt + 1
            elif arr[ni][nj] == 0:
                arr[ni][nj] = 1
                ti, tj = rear.pop(0)
                arr[ti][tj] = 0
        else:
            return cnt + 1
        cnt += 1


N = int(input())
K = int(input())
arr = [[0]*N for _ in range(N)]
for _ in range(K):
    a, b = map(int, input().split())
    arr[a-1][b-1] = 4
L = int(input())
L_list = []
D_list = []
for _ in range(L):
    a, b = input().split()
    a = int(a)
    L_list.append(a)
    D_list.append(b)
arr[0][0] = 1
L_list = L_list[::-1]
D_list = D_list[::-1]
# 입력 끝

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
# 변수 선언 끝

ans = dummy()
print(ans)
