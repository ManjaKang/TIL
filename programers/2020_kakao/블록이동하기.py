from collections import deque, defaultdict


def solution(board):
    N = len(board)
    ROW = 0
    COL = 1
    visited = defaultdict(lambda: 1000000)
    # 패딩
    arr = [[1]*(N+2)]
    for b in board:
        arr.append([1]+b+[1])
    arr.append([1]*(N+2))

    que = deque([(1, 2, ROW)])
    visited[(1, 2, ROW)] = 0
    while que:
        i, j, direct = que.popleft()

        dist = visited[i, j, direct]
        if direct == ROW:
            # 우
            ni = i
            nj = j + 1
            if arr[ni][nj] == 0 and visited[(ni, nj, ROW)] > dist+1:
                visited[(ni, nj, ROW)] = dist + 1
                que.append((ni, nj, ROW))
            # 좌
            ni = i
            nj = j - 2
            if arr[ni][nj] == 0 and visited[(i, j-1, ROW)] > dist + 1:
                visited[(i, j-1, ROW)] = dist + 1
                que.append((i, j-1, ROW))
            # 아래로 회전
            for di, dj in (1, 0), (1, -1):
                ni = i + di
                nj = j + dj
                if arr[ni][nj] == 1:
                    break
            else:
                if visited[(i+1, j, COL)] > dist + 1:
                    visited[(i+1, j, COL)] = dist + 1
                    que.append((i+1, j, COL))
                if visited[(i+1, j-1, COL)] > dist + 1:
                    visited[(i+1, j-1, COL)] = dist + 1
                    que.append((i+1, j-1, COL))
            # 위로 회전
            for di, dj in (-1, 0), (-1, -1):
                ni = i + di
                nj = j + dj
                if arr[ni][nj] == 1:
                    break
            else:
                if visited[(i, j, COL)] > dist + 1:
                    visited[(i, j, COL)] = dist + 1
                    que.append((i, j, COL))
                if visited[(i, j-1, COL)] > dist + 1:
                    visited[(i, j-1, COL)] = dist + 1
                    que.append((i, j-1, COL))
        elif direct == COL:
            # 아래
            ni = i + 1
            nj = j
            if arr[ni][nj] == 0 and visited[(ni, nj, COL)] > dist+1:
                visited[(ni, nj, COL)] = dist + 1
                que.append((ni, nj, COL))
            # 위
            ni = i - 2
            nj = j
            if arr[ni][nj] == 0 and visited[(i-1, j, COL)] > dist + 1:
                visited[(i-1, j, COL)] = dist + 1
                que.append((i-1, j, COL))
            # 우로 회전
            for di, dj in (0, 1), (-1, 1):
                ni = i + di
                nj = j + dj
                if arr[ni][nj] == 1:
                    break
            else:
                if visited[(i, j+1, ROW)] > dist + 1:
                    visited[(i, j+1, ROW)] = dist + 1
                    que.append((i, j+1, ROW))
                if visited[(i-1, j+1, ROW)] > dist + 1:
                    visited[(i-1, j+1, ROW)] = dist + 1
                    que.append((i-1, j+1, ROW))
            # 좌로 회전
            for di, dj in (0, -1), (-1, -1):
                ni = i + di
                nj = j + dj
                if arr[ni][nj] == 1:
                    break
            else:
                if visited[(i, j, ROW)] > dist + 1:
                    visited[(i, j, ROW)] = dist + 1
                    que.append((i, j, ROW))
                if visited[(i-1, j, ROW)] > dist + 1:
                    visited[(i-1, j, ROW)] = dist + 1
                    que.append((i-1, j, ROW))
    ans = min(visited[(N, N, 1)], visited[(N, N, 0)])
    return ans


_board = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]
print(solution(_board))