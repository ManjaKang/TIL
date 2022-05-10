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
        '''
        P?      ?P            P?P or P
        ?P  or  P?                   ?
                     인 경우와        P 인 경우
        '''
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

'''
Test 1 〉	통과 (0.13ms, 10.2MB)
Test 2 〉	통과 (0.07ms, 10.4MB)
Test 3 〉	통과 (0.04ms, 10.3MB)
Test 4 〉	통과 (0.04ms, 10.3MB)
Test 5 〉	통과 (0.05ms, 10.3MB)
Test 6 〉	통과 (0.03ms, 10.2MB)
Test 7 〉	통과 (0.03ms, 10.2MB)
Test 8 〉	통과 (0.05ms, 10.2MB)
Test 9 〉	통과 (0.04ms, 10.3MB)
Test 10 〉	통과 (0.04ms, 10.3MB)
Test 11 〉	통과 (0.04ms, 10.3MB)
Test 12 〉	통과 (0.04ms, 10.1MB)
Test 13 〉	통과 (0.04ms, 10.5MB)
Test 14 〉	통과 (0.03ms, 10.3MB)
Test 15 〉	통과 (0.03ms, 10.3MB)
Test 16 〉	통과 (0.03ms, 10.2MB)
Test 17 〉	통과 (0.04ms, 10.3MB)
Test 18 〉	통과 (0.04ms, 10.2MB)
Test 19 〉	통과 (0.06ms, 10.4MB)
Test 20 〉	통과 (0.05ms, 10.3MB)
Test 21 〉	통과 (0.04ms, 10.1MB)
Test 22 〉	통과 (0.04ms, 10.3MB)
Test 23 〉	통과 (0.02ms, 10.4MB)
Test 24 〉	통과 (0.03ms, 10.3MB)
Test 25 〉	통과 (0.02ms, 10.2MB)
Test 26 〉	통과 (0.02ms, 10.3MB)
Test 27 〉	통과 (0.03ms, 10.3MB)
Test 28 〉	통과 (0.03ms, 10.1MB)
Test 29 〉	통과 (0.03ms, 10.2MB)
Test 30 〉	통과 (0.04ms, 10.4MB)
Test 31 〉	통과 (0.03ms, 10.3MB)
'''