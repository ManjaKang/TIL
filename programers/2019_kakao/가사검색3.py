from collections import defaultdict


def enTrie(word, trie):
    temp_str = ''
    for ch in word:
        if ch not in trie:
            trie[temp_str] = dict()
        temp_str += ch


def searchTrie(query, trie):
    now = trie
    temp = ''
    for ch in query:
        if ch == '?':
            break
        elif ch not in now:
            return 0
        now = now[ch]
        temp += ch
    if len(now) == 0:
        return 1
    return len(now)


def solution(words, queries):
    answer = [0] * len(queries)
    trie_f = defaultdict(lambda: defaultdict(list))
    trie_b = defaultdict(lambda: defaultdict(list))
    led_list = []
    for word in words:
        enTrie(word, trie_f[len(word)])
        enTrie(word[::-1], trie_b[len(word)])
        led_list.append(len(word))

    for i, query in enumerate(queries):
        if query[0] == '?' and query[-1] == '?':
            direction = 'both'
        elif query[0] == '?':
            direction = 'back'
        elif query[-1] == '?':
            direction = 'front'

        if direction == 'both':
            answer[i] = led_list.count(len(query))

        elif direction == 'front':
            answer[i] = searchTrie(query, trie_f[len(query)])

        elif direction == 'back':
            answer[i] = searchTrie(query[::-1], trie_b[len(query)])
    return answer


words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]

print(solution(words, queries))
trie = defaultdict(lambda: defaultdict(list))
for word in words:
    enTrie(word, trie[len(word)])

print(len(trie[5]['f']))



