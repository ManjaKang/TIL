from itertools import combinations


def chicken_dist(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
house_list = []
chicken_list = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            house_list.append((i, j))
        elif arr[i][j] == 2:
            chicken_list.append((i, j))

case_list = list(combinations(range(len(chicken_list)), M))
min_dist = 10000000

for case in case_list:
    temp_sum = 0
    for house in house_list:
        temp_chi = 10000000
        for chi_idx in case:
            temp_chi = min(temp_chi, chicken_dist(house, chicken_list[chi_idx]))
        temp_sum += temp_chi
    min_dist = min(min_dist, temp_sum)

print(min_dist)

