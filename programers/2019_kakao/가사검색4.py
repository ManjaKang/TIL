from collections import defaultdict


def enTrie(word, trie):
    temp = ''@
    for i in range(len(word)):
        temp += word[i]
        trie[temp] += 1


def searchTrie(query, trie):
    temp = ''
    for ch in query:
        if ch == '?':
            break
        temp += ch
    return trie[temp]


def solution(words, queries):

    trie_f = defaultdict(lambda: defaultdict(int))
    trie_b = defaultdict(lambda: defaultdict(int))
    answer = [0] * len(queries)
    len_list = []
    for word in words:
        enTrie(word, trie_f[len(word)])
        enTrie(word[::-1], trie_b[len(word)])
        len_list.append(len(word))

    for i, query in enumerate(queries):
        direction = 'both'
        if query[-1] != '?':
            direction = 'back'
        elif query[0] != '?':
            direction = 'front'

        if direction == 'both':
            answer[i] = len_list.count(len(query))

        elif direction == 'front':
            answer[i] = searchTrie(query, trie_f[len(query)])

        elif direction == 'back':
            answer[i] = searchTrie(query[::-1], trie_b[len(query)])
    return answer


words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
print(solution(words, queries))