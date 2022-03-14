def abs_num(n):
    if n >= 0:
        return n
    else:
        return -n


# 두 점을 이용해 넒이를 구하는 함수
def area(a, b):
    if a[0] == b[0] or a[1] == b[1]:
        return 0
    width = a[0] - b[0]
    height = a[1] - b[1]
    return abs_num(width * height)


# 방향 거리를 입력받아 x, y 좌표를 이동하는 함수
def locale(d, s, x, y):
    if d == 1:
        return x + s, y
    if d == 2:
        return x - s, y
    if d == 3:
        return x, y - s
    if d == 4:
        return x, y + s


# 7가지 점중에서 가운데 있는 점을 찾는 함수
# 모든 점에서 x, y의 최대, 최솟값을 찾고
# 이 값을 하나도 가지지 않는 좌표가 중앙
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
    # 중앙을 못찾으면 0, 0 을 반환
    return 0, 0


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
# 중앙에서 나머지 모든 점들과 넒이를 구해 합치면 참외밭의 넓이가 나옴
for location in locations:
    ans_list.append(area(center, location))

print(sum(ans_list) * N)

