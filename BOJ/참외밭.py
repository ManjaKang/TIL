def abs_num(n):@
    if n >= 0:
        return n
    else:
        return -n


def area(a, b):
    if a[0] == b[0] or a[1] == b[1]:
        return 0
    width = a[0] - b[0]
    height = a[1] - b[1]
    return abs_num(width * height)


def locale(d, s, x, y):
    if d == 1:
        return x + s, y
    if d == 2:
        return x - s, y
    if d == 3:
        return x, y - s
    if d == 4:
        return x, y + s


def findCenter(locs):
    max_x = locs[0][0]
    max_y = locs[0][1]
    min_x = locs[0][0]
    min_y = locs[0][1]
    for loc in locs:
        if max_x < loc[0]:
            max_x = loc[0]
        if max_y < loc[1]:
            max_y = loc[1]
        if min_x > loc[0]:
            min_x = loc[0]
        if min_y > loc[1]:
            min_y = loc[1]
    for loc in locs:
        if max_x == loc[0]:
            continue
        if max_y == loc[1]:
            continue
        if min_x == loc[0]:
            continue
        if min_y == loc[1]:
            continue
        return loc
    return (0, 0)



N = int(input())
dir_list = []
side_list = []
for _ in range(6):
    D, S = map(int, input().split())
    dir_list.append(D)
    side_list.append(S)

locations = [(0, 0)]
for i in range(5):
    location = locale(dir_list[i], side_list[i], *locations[i])
    locations.append(location)

center = findCenter(locations)
ans_list = []
for location in locations:
    ans_list.append(area(center, location))

print(sum(ans_list) * N)

