x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

a = y2 - y1
b = x1 - x2
c = y4 - y3
d = x3 - x4
p = (x1 - x2) * y1 + (y2 - y1) * x1
q = (x3 - x4) * y3 + (y4 - y3) * x3
idx = a * d - b * c
temp_x = d * p - b * q
temp_y = a * q - c * p
ans = 0
same = False
trans = False
same_inclination_point = False
x1, x2 = min(x1, x2), max(x1, x2)
x3, x4 = min(x3, x4), max(x3, x4)
y1, y2 = min(y1, y2), max(y1, y2)
y3, y4 = min(y3, y4), max(y3, y4)

if idx:
    if idx < 0:
        temp_x *= -1
        temp_y *= -1
        idx *= -1
        trans = True
    if x1 * idx <= temp_x <= x2 * idx and y1 * idx <= temp_y <= y2 * idx:
        if x3 * idx <= temp_x <= x4 * idx and y3 * idx <= temp_y <= y4 * idx:
            ans = 1
else:
    # 두 선분이 한 직선 위에 있을 때
    if (y1 - y2) * (x3 - x1) == (y3 - y1) * (x1 - x2):
        # 수직 직선
        if x1 == x2:
            if y1 <= y3 < y2 or y3 <= y1 < y4:
                ans = 1
                same = True
        # 나머지
        elif x1 <= x3 < x2 or x3 <= x1 < x4:
            ans = 1
            same = True

        if x1 < x3 and x2 == x3:
            ans = 1
            same_inclination_point = True
            tx = x2
            ty = y2
        if x3 < x1 and x2 == x4:
            ans = 1
            same_inclination_point = True
            tx = x2
            ty = y2

        if y1 < y3 == y2:
            ans = 1
            same_inclination_point = True
            tx = x2
            ty = y2
        if y3 < y1 == y4:
            ans = 1
            same_inclination_point = True
            tx = x1
            ty = y1

if ans:
    if same:
        print(1)
    else:
        if same_inclination_point:
            x = tx
            y = ty
        else:
            x = temp_x / idx
            y = temp_y / idx
        print(1)
        print(x, y)
else:
    print(0)
