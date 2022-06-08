# PyPy 112ms

def find_parent(a):
    if parent[a] != a:
        parent[a] = find_parent(parent[a])
    return parent[a]


def union(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


N, M = map(int, input().split())
parent = [i for i in range(N+1)]
truth = list(map(int, input().split()))
truth_parent = 0
arr = []
# 변수 선언 끝

# 진실을 아는 사람들을 한 집합으로
for i in range(1, truth[0]):
    union(truth[i], truth[i + 1])

# 각 파티에 참가하는 사람들을 한 집합으로
for i in range(M):
    arr.append(list(map(int, input().split())))
    for j in range(1, arr[i][0]):
        union(arr[i][j], arr[i][j+1])

# 진실을 아는 사람의 부모를 찾기
if truth[0] != 0:
    truth_parent = find_parent(truth[-1])
ans = 0

# 각 파티의 부모가 진실을 아는 사람의 부모와 다르면 ans += 1
for i in range(M):
    if truth_parent != find_parent(arr[i][-1]):
        ans += 1
print(ans)