def perm_dfs():
    if len(now) == R:
        ans_list.append(now[:])
        return
    for i in range(N):
        if visited[i] == 0:
            now.append(target_list[i])
            visited[i] = 1
            perm_dfs()
            now.pop()
            visited[i] = 0
    return


def comb_dfs(s):
    if len(now) == R:
        ans_list.append(now[:])
        return
    for i in range(s, N):
        if visited[i] == 0:
            visited[i] = 1
            now.append(target_list[i])
            comb_dfs(i+1)
            visited[i] = 0
            now.pop()
    return


def perm_repeat_dfs():
    if len(now) == R:
        ans_list.append(now[:])
        return
    for i in range(N):&
        now.append(target_list[i])
        perm_dfs()
        now.pop()
    return


def comb_repeat_dfs(s):
    if len(now) == R:
        ans_list.append(now[:])
        return
    for i in range(s, N):
        now.append(target_list[i])
        comb_repeat_dfs(s)
        now.pop()
        s += 1
    return


target_list = [1, 2, 3]
N = 3
R = 2
ans_list = []
now = []
visited = [0] * N

comb_repeat_dfs(0)
print(ans_list)