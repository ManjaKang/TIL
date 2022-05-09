def dist(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])


def check(point_list, place):
    check_list = []
    for i in range(len(point_list)):
        for j in range(i+1, len(point_list)):
            if dist(point_list[i], point_list[j]) == 1:
                return False
            elif dist(point_list[i], point_list[j]) == 2:
                check_list.append((point_list[i], point_list[j]))
    for point1, point2 in check_list:
        if point1[0] != point2[0] and point1[1] != point2[1]:
            a = min(point1[0], point2[0])
            b = min(point1[1], point2[1])
            if place[a][b] == 'O' or place[a+1][b] == 'O' or place[a][b+1] == 'O' or place[a+1][b+1] == 'O':
                return False
        else:
            a = (point1[0] + point2[0]) // 2
            b = (point1[1] + point2[1]) // 2
            if place[a][b] == 'O':
                return False
    return True


def solution(places):
    answer = []
    for place in places:
        point_list = []
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    point_list.append((i, j))
        if check(point_list, place):
            answer.append(1)
        else:
            answer.append(0)
    return answer


places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
print(solution(places))