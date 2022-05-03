def build_beam(arr_c, arr_b, x, y):
    if arr_c[x][y-1] == 0 or arr_c[x+1][y-1] == 0:
        arr_b[x][y] = 1
        return
    if arr_b[x-1][y] == 1 and arr_b[x+1][y] == 1:
        arr_b[x][y] = 1
        return


def build_col(arr_c, arr_b, x, y):
    if y == 0:
        arr_c[x][y] = 0
        return
    if arr_c[x][y-1] == 0 or arr_b[x][y] == 1 or arr_b[x-1][y] == 1:
        arr_c[x][y] = 0
        return


def is_it_ok(arr_c, arr_b, x, y):
    if arr_b[x][y] == 1:
        if arr_c[x][y-1] == 0 or arr_c[x+1][y-1] == 0:
            return True
        if arr_b[x-1][y] == 1 and arr_b[x+1][y] == 1:
            return True
        return False
    elif arr_c[x][y] == 0:
        if arr_c[x][y-1] == 0:
            return True
        if arr_b[x-1][y] == 1 or arr_b[x][y] == 1:
            return True
        return False
    return True


def del_col(arr_c, arr_b, x, y):
    arr_c[x][y] = -1
    if is_it_ok(arr_c, arr_b, x, y+1) and is_it_ok(arr_c, arr_b, x+1, y+1) and is_it_ok(arr_c, arr_b, x-1, y+1):
        return
    arr_c[x][y] = 0
    return


def del_beam(arr_c, arr_b, x, y):
    arr_b[x][y] = -1
    if is_it_ok(arr_c, arr_b, x+1, y) and is_it_ok(arr_c, arr_b, x-1, y) and is_it_ok(arr_c, arr_b, x, y):
        return
    arr_b[x][y] = 1
    return


def solution(n, build_frame):
    arr_c = [[-1]*(n+1) for _ in range(n+1)]
    arr_b = [[-1]*(n+1) for _ in range(n+1)]

    for build in build_frame:
        x, y, a, b = build
        if a:
            if b:
                build_beam(arr_c, arr_b, x, y)
            else:
                del_beam(arr_c, arr_b, x, y)
        else:
            if b:
                build_col(arr_c, arr_b, x, y)
            else:
                del_col(arr_c, arr_b, x, y)
    ans = []
    for x in range(n+1):
        for y in range(n+1):
            if arr_c[x][y] == 0:
                ans.append([x, y, 0])
            if arr_b[x][y] == 1:
                ans.append([x, y, 1])
    return ans


build = 	[[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
build2 = 	[[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]
print(solution(5, build2))