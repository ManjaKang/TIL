import sys
import itertools
from copy import deepcopy
sys.stdin = open('sample_input.txt', 'r')


def cal_dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def down(dis_list, case):
    dis_list = deepcopy(dis_list)
    cnt = 0
    time = 0
    visited = [0] * num_people
    global ans
    while cnt < num_people:
        time += 1
        for entrance in entrances:
            for i in range(len(entrance) - 1, -1, -1):
                entrance[i] -= 1
                if entrance[i] == 0:
                    cnt += 1
                    entrance.pop(i)

        for idx, i in enumerate(case):
            if dis_list[idx][i] == 0 and len(entrances[i]) < 3 and visited[idx] == 0:
                entrances[i].append(len_entrances[i])
                visited[idx] = 1
            if dis_list[idx][i] != 0:
                dis_list[idx][i] -= 1
    ans = min(ans, time)
    return


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    entrances_position = []
    people = []
    len_entrances = []
    entrances = [[], []]
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                people.append((i, j))
            elif arr[i][j] != 0:
                entrances_position.append((i, j))
                len_entrances.append(arr[i][j])

    distances = []
    for person in people:
        distances.append([cal_dist(entrances_position[0], person), cal_dist(entrances_position[1], person)])

    num_people = len(people)
    case_list = list(itertools.product((0, 1), repeat=num_people))
    ans = 1000000
    for case in case_list:
        down(distances, case)

    print('#{} {}'.format(tc, ans))
