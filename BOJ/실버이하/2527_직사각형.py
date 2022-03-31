for _ in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2, = map(int, input().split())
    x_list = [x1, p1, x2, p2]
    y_list = [y1, q1, y2, q2]
    x_list = list(set(x_list))
    y_list = list(set(y_list))
    if len(x_list) + len(y_list) == 4:
        ans = 'a'
    elif
    print(x_list, y_list)