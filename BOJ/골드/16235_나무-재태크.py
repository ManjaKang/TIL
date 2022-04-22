# s2
# PyPy 952ms
from collections import defaultdict

N, M, K = map(int, input().split())
arr = [[5] * N for _ in range(N)]
fer_arr = [list(map(int, input().split())) for _ in range(N)]
tree_dict = defaultdict(lambda: defaultdict(list))
for _ in range(M):
    x, y, z = map(int, input().split())
    x -= 1
    y -= 1
    tree_dict[x][y].append(z)
di = [0, 1, 0, -1, 1, 1, -1, -1]
dj = [1, 0, -1, 0, 1, -1, 1, -1]

for _ in range(K):
    # 봄, 여름
    for i, row in tree_dict.items():
        for j, trees in row.items():
            trees.sort(reverse=True)
            fer = 0
            for idx in range(len(trees) - 1, -1, -1):  # for 문에서 in 뒤에 있는 len은 처음에 한번만 계산
                if arr[i][j] >= trees[idx]:
                    arr[i][j] -= trees[idx]
                    trees[idx] += 1
                else:
                    fer += trees.pop(idx) // 2
            arr[i][j] += fer

    # 가을
    new_tree = []
    for i, row in tree_dict.items():
        for j, trees in row.items():
            for tree in trees:
                if not tree % 5:
                    for idx in range(8):
                        ni = i + di[idx]
                        nj = j + dj[idx]
                        if 0 <= ni < N and 0 <= nj < N:
                            new_tree.append((ni, nj))
    for i, j in new_tree:
        tree_dict[i][j].append(1)

    # 겨울
    for i in range(N):
        for j in range(N):
            arr[i][j] += fer_arr[i][j]

ans = 0
for row in tree_dict.values():
    for trees in row.values():
        ans += len(trees)

print(ans)
