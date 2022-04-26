# PyPy 280ms
# Trie 자료 구조를 이용한 풀이
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    number_list = [input() for _ in range(N)]

    trie = dict()
    ans = 0
    number_list.sort()
    for number_str in number_list:
        now = trie
        for ch in number_str:
            if 'END' in now:
                ans = 'NO'
                break
            if ch not in now:
                now[ch] = dict()
            now = now[ch]
        if 'END' not in now:
            now['END'] = 1
        if ans:
            break
    if not ans:
        ans = 'YES'
    print(ans)
