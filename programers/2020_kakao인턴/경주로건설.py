from collections import deque


def bfs(board):
    N = len(board)
    visited_row = [[float('inf')] * N for _ in range(N)]
    visited_col = [[float('inf')] * N for _ in range(N)]
    visited_row[0][0] = 0
    visited_col[0][0] = 0
    que = deque([(0, 0, 0), (0, 0, 1)])
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    while que:
        i, j, d = que.popleft()         # d는 이전 방향 1 => 가로, 0 => 세로
        if d:
            dist = visited_row[i][j]
        else:
            dist = visited_col[i][j]

        for idx in range(4):
            ni = i + di[idx]
            nj = j + dj[idx]
            if (idx + d) % 2:           # (idx + d) % 2 로 이전 방향과 같은지 방향이 바꼈는지 알 수 있음
                cost = 6
            else:
                cost = 1
            if 0 <= ni < N and 0 <= nj < N:
                # 가로이면
                if idx % 2:
                    if not board[ni][nj] and visited_row[ni][nj] > dist + cost:
                        visited_row[ni][nj] = dist + cost
                        que.append((ni, nj, idx % 2))
                # 세로이면
                else:
                    if not board[ni][nj] and visited_col[ni][nj] > dist + cost:
                        visited_col[ni][nj] = dist + cost
                        que.append((ni, nj, idx % 2))
    return min(visited_row[-1][-1], visited_col[-1][-1]) * 100


def solution(board):
    return bfs(board)


'''
Test 1 〉	통과 (0.04ms, 10.3MB)
Test 2 〉	통과 (0.02ms, 10.4MB)
Test 3 〉	통과 (0.02ms, 10.3MB)
Test 4 〉	통과 (0.07ms, 10.2MB)
Test 5 〉	통과 (0.05ms, 10.3MB)
Test 6 〉	통과 (0.43ms, 10.3MB)
Test 7 〉	통과 (0.47ms, 10.3MB)
Test 8 〉	통과 (0.57ms, 10.3MB)
Test 9 〉	통과 (0.41ms, 10.2MB)
Test 10 〉	통과 (0.81ms, 10.3MB)
Test 11 〉	통과 (3.88ms, 10.3MB)
Test 12 〉	통과 (2.87ms, 10.3MB)
Test 13 〉	통과 (0.24ms, 10.3MB)
Test 14 〉	통과 (0.20ms, 10.3MB)
Test 15 〉	통과 (0.61ms, 10.3MB)
Test 16 〉	통과 (1.08ms, 10.3MB)
Test 17 〉	통과 (1.38ms, 10.4MB)
Test 18 〉	통과 (1.86ms, 10.4MB)
Test 19 〉	통과 (1.76ms, 10.4MB)
Test 20 〉	통과 (1.56ms, 10.4MB)
Test 21 〉	통과 (1.17ms, 10.3MB)
Test 22 〉	통과 (0.16ms, 10.2MB)
Test 23 〉	통과 (0.08ms, 10.3MB)
Test 24 〉	통과 (0.08ms, 10.3MB)
Test 25 〉	통과 (0.05ms, 10.3MB)
'''