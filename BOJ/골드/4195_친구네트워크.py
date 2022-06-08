def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])
    return parent[a]


def union(a, b):
    a = find(a)
    b = find(b)
    if a > b:
        parent[a] = b
        len_list[b] += len_list[a]
    elif a < b:
        parent[b] = a
        len_list[a] += len_list[b]


T = int(input())
for _ in range(T):
    F = int(input())
    friend_dict = dict()
    index = 0
    parent = []
    len_list = []
    for _ in range(F):
        A, B = input().split()
        if A not in friend_dict:
            friend_dict[A] = index
            parent.append(index)
            index += 1
            len_list.append(1)
        if B not in friend_dict:
            friend_dict[B] = index
            parent.append(index)
            index += 1
            len_list.append(1)
        union(friend_dict[A], friend_dict[B])
        print(len_list[find(friend_dict[A])])
