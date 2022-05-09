from collections import Counter
import sys
input = sys.stdin.readline


def check(x1, y1, x2, y2, x3, y3, x4, y4):
    a = y2 - y1
    b = x1 - x2
    c = y4 - y3
    d = x3 - x4
    p = (x1 - x2) * y1 + (y2 - y1) * x1
    q = (x3 - x4) * y3 + (y4 - y3) * x3
    idx = a * d - b * c
    temp_x = d * p - b * q
    temp_y = a * q - c * p
    x1, x2 = min(x1, x2), max(x1, x2)
    x3, x4 = min(x3, x4), max(x3, x4)
    y1, y2 = min(y1, y2), max(y1, y2)
    y3, y4 = min(y3, y4), max(y3, y4)

    if idx:
        if idx < 0:
            temp_x *= -1
            temp_y *= -1
            idx *= -1
        if x1 * idx <= temp_x <= x2 * idx and y1 * idx <= temp_y <= y2 * idx:
            if x3 * idx <= temp_x <= x4 * idx and y3 * idx <= temp_y <= y4 * idx:
                return True
    # else:
    #     # 두 선분이 한 직선 위에 있을 때
    #     if (y1 - y2) * (x3 - x1) == (y3 - y1) * (x1 - x2):
    #         # 수직 직선
    #         if x1 == x2:
    #             if y1 <= y3 <= y2 or y3 <= y1 <= y4:
    #                 return True
    #         # 나머지
    #         elif x1 <= x3 <= x2 or x3 <= x1 <= x4:
    #             return True
    return False


def getP(a):
    if p[a] == a:
        return a
    else:
        p[a] = getP(p[a])
        return p[a]


def union(a, b):
    p_a = getP(a)
    p_b = getP(b)
    if p_a > p_b:
        p[p_a] = p_b
    elif p_a < p_b:
        p[p_b] = p_a


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [0] * N
ans_list = []
p = [i for i in range(N)]

if N == 1:
    print(1)
    print(1)
else:
    for i in range(N-1):
        x1, y1, x2, y2 = arr[i]
        for j in range(i+1, N):
            x3, y3, x4, y4 = arr[j]
            if check(x1, y1, x2, y2, x3, y3, x4, y4):
                union(i, j)
    counter = dict(Counter(p))
    cnt = 0
    for i in range(N):
        if p[i] == i:
            cnt += 1
    print(cnt)
    print(max(counter.values()))