from collections import defaultdict


def enTrie(word):
    now = trie
    for ch in word:
        if now.get(ch) is None:
            now[ch] = defaultdict(int)
        now = now[ch]
        now['_depth'] += 1


def searchTrie(word):
    rlt = 0
    now = trie
    prev = 0
    for ch in word:
        now = now[ch]
        if prev != now['_depth']:
            rlt += 1
        prev = now['_depth']
    return rlt


while True:
    try:
        N = int(input())
        arr = [input() for _ in range(N)]
        trie = dict()
        ans = 0
        for word in arr:
            enTrie(word)
        for word in arr:
            ans += searchTrie(word)
        ans /= len(arr)
        print(f'{ans:.2f}')
    except:
        break
