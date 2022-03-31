def comb_dfs(s):
    if len(now) == 6:
        ans_list.append(now[:])
        return

    for i in range(s, K):
        if visited[i] == 0:
            visited[i] = 1
            now.append(S[i])
            comb_dfs(i+1)
            visited[i] = 0
            now.pop()
    return


while True:
    nums = list(map(int, input().split()))
    K = nums[0]
    if K == 0:
        break
    S = nums[1:]
    # 입력 끝

    visited = [0] * K
    now = []
    ans_list = []
    # 변수 선언 끝

    comb_dfs(0)
    for ans in ans_list:
        print(*ans)
    print()