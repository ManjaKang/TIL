def post(n):
    for child in children[n]:
        post(child)
    if n == 0:
        return
    num_descendants[parent[n]] += num_descendants[n]


N = int(input())
parent = list(map(int, input().split()))
children = [[] for _ in range(N)]
num_children = [0] * N
for i, p in enumerate(parent[1:]):
    children[p].append(i+1)
    num_children[p] += 1

num_descendants = num_children[:]
post(0)

now = 0
max_descendants = 0
temp_child = 0
ans = 0
while True:
    max_descendants = 0
    for child in children[now]:
        if max_descendants < num_descendants[child]:
            max_descendants = num_descendants[child]
            temp_child = child
    if max_descendants == 0:
        ans += num_children[now]
        break
    ans += 1
    now = temp_child

print(ans)