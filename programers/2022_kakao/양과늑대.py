from collections import defaultdict


def solution(info, edges):

    visited = defaultdict(list)
    adj_dict = defaultdict(list)
    # edges를 인접 딕셔너리로 바꿔줌
    for a, b in edges:
        adj_dict[a].append(b)
        adj_dict[b].append(a)
    ans = 1                     # 0 지점에는 항상 양이 있으므로 1로 초기화

    def dfs(i, n, m):
        # 종료 조건
        if n == m:
            return

        for a in adj_dict[i]:
            # 늑대가 있는 경우
            if info[a] == 1 and (n, m+1) not in visited[a]:
                visited[a].append((n, m+1))
                info[a] = -1
                dfs(a, n, m+1)
                info[a] = 1
                visited[a].pop()
            # 양이 있는 경우
            elif info[a] == 0 and (n+1, m) not in visited[a]:
                visited[a].append((n+1, m))
                info[a] = -1
                nonlocal ans
                ans = max(ans, n+1)
                dfs(a, n+1, m)
                info[a] = 0
                visited[a].pop()
            # 아무것도 없는 경우
            elif (n, m) not in visited[a]:
                visited[a].append((n, m))
                dfs(a, n, m)
                visited[a].pop()

    info[0] = -1
    visited[0].append((1, 0))
    dfs(0, 1, 0)

    return ans


'''
Test 1 〉	통과 (0.01ms, 10.1MB)
Test 2 〉	통과 (1.06ms, 10.2MB)
Test 3 〉	통과 (0.02ms, 10.2MB)
Test 4 〉	통과 (0.02ms, 10.2MB)
Test 5 〉	통과 (5.33ms, 10.2MB)
Test 6 〉	통과 (0.86ms, 10.3MB)
Test 7 〉	통과 (0.19ms, 10.4MB)
Test 8 〉	통과 (0.10ms, 10.4MB)
Test 9 〉	통과 (1.45ms, 10.2MB)
Test 10 〉	통과 (37.26ms, 10.3MB)
'''