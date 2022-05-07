def enTrie(arr):
    now = trie
    depth = 0
    for word in arr:
        if now.get(word) is None:
            now[word] = dict()
        now['_depth'] = depth
        depth += 1
        now = now[word]


def preorder(trie):
    for key in trie:
        if key == '_depth':
            continue
        print('--'*trie['_depth'], end='')
        print(key)
        preorder(trie[key])


N = int(input())
arr = []
for _ in range(N):
    ar = list(input().split())
    ar = ar[1:]
    arr.append(ar)

arr.sort()
trie = dict()
for ar in arr:
    enTrie(ar)
preorder(trie)