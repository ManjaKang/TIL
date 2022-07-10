# PyPy 3300ms
from itertools import combinations

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
N, M, G, R = map(int, input().split())
arr = [[0]*(M+2)] +\
      [[0] + list(map(int, input().split())) + [0] for _ in range(N)] +\
      [[0]*(M+2)]

soils = []
for i in range(1, N+1):
    for j in range(1, M+1):
        if arr[i][j] == 2:
            soils.append((i, j))

# 배양액 놓는 모든 경우의 수 구하기
soil_set = set(range(len(soils)))
case_list = []
green_set = set(combinations(soil_set, G))
ans = 0
for green in green_set:
    temp_set = soil_set - set(green)
    red_set = set(combinations(temp_set, R))
    for red in red_set:
        case_list.append([green, red])


def check(case):
    greens = case[0]
    reds = case[1]
    green_stack = []
    red_stack = []
    rlt = 0
    flag = True
    map = [a[:] for a in arr]
    for green in greens:
        i, j = soils[green]
        green_stack.append((i, j))
        map[i][j] = 0
    for red in reds:
        i, j = soils[red]
        red_stack.append((i, j))
        map[i][j] = 0

    while flag:
        flag = False
        temp_green = set()
        temp_red = set()
        while green_stack:
            i, j = green_stack.pop()
            for idx in range(4):
                ni = i + di[idx]
                nj = j + dj[idx]
                if map[ni][nj]:
                    temp_green.add((ni, nj))
                    flag = True

        while red_stack:
            i, j = red_stack.pop()
            for idx in range(4):
                ni = i + di[idx]
                nj = j + dj[idx]
                if map[ni][nj]:
                    flag = True
                    temp_red.add((ni, nj))

        flower = temp_green & temp_red
        for i, j in flower:
            rlt += 1
        for i, j in temp_green | temp_red:
            map[i][j] = 0
        green_stack = list(temp_green - flower)
        red_stack = list(temp_red - flower)
    return rlt


for case in case_list:
    ans = max(ans, check(case))

print(ans)







