def snail(result_list, x, y, direction, n, i):
    if i > n**2:
        return result_list
    
    if direction == 1:
        if x == n - 1:
            direction = 2
            return snail(result_list, x, y, direction, n, i)
        if result_list[y][x+1] != 0:
            direction = 2
            return snail(result_list, x, y, direction, n, i)
        result_list[y][x+1] = i
        i += 1
        return snail(result_list, x+1, y, direction, n, i)

    if direction == 2:
        if y == n - 1:
            direction = 3
            return snail(result_list, x, y, direction, n, i)
        if result_list[y+1][x] != 0:
            direction = 3
            return snail(result_list, x, y, direction, n, i)
        result_list[y+1][x] = i
        i += 1
        return snail(result_list, x, y+1, direction, n, i)

    if direction == 3:
        if x == 0:
            direction = 4
            return snail(result_list, x, y, direction, n, i)
        if result_list[y][x-1] != 0:
            direction = 4
            return snail(result_list, x, y, direction, n, i)
        result_list[y][x-1] = i
        i += 1
        return snail(result_list, x-1, y, direction, n, i)

    if direction == 4:
        if y == 0:
            direction = 1
            return snail(result_list, x, y, direction, n, i)
        if result_list[y-1][x] != 0:
            direction = 1
            return snail(result_list, x, y, direction, n, i)
        result_list[y-1][x] = i
        i += 1
        return snail(result_list, x, y-1, direction, n, i)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    result_list = [[0]*N for i in range(N)]
    direction = 1
    result_list[0][0] = 1
    x, y = 0, 0
    res = snail(result_list, x, y, direction, N, 2)
    for i in range(N):
        for j in range(N):
            print(res[i][j],end = ' ')
        print()
        
