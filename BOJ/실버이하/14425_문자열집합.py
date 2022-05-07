import sys
input = sys.stdin.readline


def enTrie(word):
    now = trie
    for ch in word:
        if ch not in now:
            now[ch] = dict()
        now = now[ch]
    now['_end'] = '_end'


def searchTrie(word):
    now = trie
    for ch in word:
        if ch not in now:
            return False
        now = now[ch]
    if '_end' in now:
        return True
    return False


N, M = map(int, input().split())
arr_N = [input().strip() for _ in range(N)]
arr_M = [input().strip() for _ in range(M)]
trie = dict()
for word in arr_N:
    enTrie(word)

ans = 0
for word in arr_M:
    if searchTrie(word):
        ans += 1
print(ans)