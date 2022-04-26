from collections import defaultdict


def enTrie(word, trie):
    len_word = len(word)
    now = trie
    for ch in word:
        now[len_word] += 1
        if ch not in now:
            now[ch] = defaultdict(int)
        now = now[ch]


def searchTrie(word, trie):
    len_word = len(word)
    now = trie
    for ch in word:
        if ch == '?':
            return now[len_word]
        if ch not in now:
            return 0
        now = now[ch]


def solution(words, queries):

    trie_f = defaultdict(int)
    trie_b = defaultdict(int)
    answer = [0] * len(queries)

    for word in words:
        enTrie(word, trie_f)
        enTrie(word[::-1], trie_b)

    for i, query in enumerate(queries):
        if query[-1] == '?':
            answer[i] = searchTrie(query, trie_f)

        else:
            answer[i] = searchTrie(query[::-1], trie_b)
    return answer


'''
Test 1 〉	통과 (722.79ms, 134MB)
Test 2 〉	통과 (1347.32ms, 237MB)
Test 3 〉	통과 (1304.51ms, 235MB)
Test 4 〉	통과 (1101.87ms, 252MB)
Test 5 〉	통과 (2122.43ms, 508MB)
'''