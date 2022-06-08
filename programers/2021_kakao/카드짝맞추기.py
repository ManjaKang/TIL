from itertools import permutations
from collections import defaultdict, deque


def bfs(board, start, end):
    visited = [[1000]*4 for _ in range(4)]
    visited[start[0]][start[1]] = 0
    que = deque([start])
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    while que:
        i, j = que.popleft()
        dist = visited[i][j]
        # 기본 이동
        for idx in range(4):
            ni = i + di[idx]
            nj = j + dj[idx]
            if 0 <= ni < 4 and 0 <= nj < 4 and visited[ni][nj] > dist + 1:
                visited[ni][nj] = dist + 1
                que.append((ni, nj))
        # 컨트롤 이동
        for idx in range(4):
            for k in range(1, 4):
                ni = i + di[idx] * k
                nj = j + dj[idx] * k
                if not (0 <= ni < 4 and 0 <= nj < 4):
                    ni -= di[idx]
                    nj -= dj[idx]
                    break
                else:
                    if board[ni][nj] != 0:
                        break
            if visited[ni][nj] > dist + 1:
                visited[ni][nj] = dist + 1
                que.append((ni, nj))

    return visited[end[0]][end[1]]


def solution(board, r, c):
    num_set = set()
    num_dict = defaultdict(list)
    for i in range(4):
        for j in range(4):
            if board[i][j] != 0:
                num_set.add(board[i][j])
                num_dict[board[i][j]].append((i, j))
    case_list = list(permutations(num_set, len(num_set)))
    answer = 10000
    for case in case_list:
        temp_ans = 0
        temp_board = [item[:] for item in board]
        now_r = r
        now_c = c
        for card in case:
            path1 = bfs(temp_board, (now_r, now_c), num_dict[card][0]) + bfs(temp_board, num_dict[card][0], num_dict[card][1])
            path2 = bfs(temp_board, (now_r, now_c), num_dict[card][1]) + bfs(temp_board, num_dict[card][1], num_dict[card][0])
            temp_board[num_dict[card][0][0]][num_dict[card][0][1]] = 0
            temp_board[num_dict[card][1][0]][num_dict[card][1][1]] = 0
            # 그리디 하게 짧은 길을 선택
            # 이동이 복잡할 경우에는 완전 탐색이 더 좋아 보임
            if path1 > path2:
                now_r = num_dict[card][0][0]
                now_c = num_dict[card][0][1]
                temp_ans += path2
            else:
                now_r = num_dict[card][1][0]
                now_c = num_dict[card][1][1]
                temp_ans += path1
        answer = min(answer, temp_ans)
    return answer + len(num_dict) * 2       # 마지막에 엔터에 사용된 횟수를 더함


'''
Test 1 〉	통과 (4.65ms, 10.2MB)
Test 2 〉	통과 (4.78ms, 10.3MB)
Test 3 〉	통과 (4.63ms, 10.4MB)
Test 4 〉	통과 (4.77ms, 10.4MB)
Test 5 〉	통과 (23.75ms, 10.2MB)
Test 6 〉	통과 (24.15ms, 10.2MB)
Test 7 〉	통과 (24.36ms, 10.3MB)
Test 8 〉	통과 (24.55ms, 10.3MB)
Test 9 〉	통과 (144.78ms, 10.3MB)
Test 10 〉	통과 (147.95ms, 10.4MB)
Test 11 〉	통과 (149.40ms, 10.2MB)
Test 12 〉	통과 (148.00ms, 10.3MB)
Test 13 〉	통과 (1044.88ms, 10.4MB)
Test 14 〉	통과 (1051.55ms, 10.4MB)
Test 15 〉	통과 (1028.57ms, 10.4MB)
Test 16 〉	통과 (1030.12ms, 10.4MB)
Test 17 〉	통과 (0.57ms, 10.5MB)
Test 18 〉	통과 (0.29ms, 10.3MB)
Test 19 〉	통과 (1.10ms, 10.4MB)
Test 20 〉	통과 (1.08ms, 10.4MB)
Test 21 〉	통과 (37.58ms, 10.3MB)
Test 22 〉	통과 (1064.05ms, 10.4MB)
Test 23 〉	통과 (1071.02ms, 10.2MB)
Test 24 〉	통과 (24.46ms, 10.5MB)
Test 25 〉	통과 (1051.80ms, 10.4MB)
Test 26 〉	통과 (24.25ms, 10.3MB)
Test 27 〉	통과 (28.92ms, 10.4MB)
Test 28 〉	통과 (4.70ms, 10.4MB)
Test 29 〉	통과 (4.64ms, 10.5MB)
Test 30 〉	통과 (4.59ms, 10.4MB)
'''