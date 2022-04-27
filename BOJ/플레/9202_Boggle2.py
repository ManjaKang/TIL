from copy import deepcopy


def enTrie(word):
    now = Trie
    for ch in word:
        if ch not in now:
            now[ch] = dict()
        now = now[ch]
    now['_end'] = '_end'


def dfs(i, j, word, now: dict):
    if '_end' in now:
        now.pop('_end')
        ans_list.append(word)

    for idx in range(8):
        ni = i + di[idx]
        nj = j + dj[idx]
        if 0 <= ni < 4 and 0 <= nj < 4:
            if visited[ni][nj] == 0 and board[ni][nj] in now:
                visited[ni][nj] = 1
                dfs(ni, nj, word+board[ni][nj], now[board[ni][nj]])
                visited[ni][nj] = 0


W = int(input())
arr_word = [input() for _ in range(W)]
input()
B = int(input())
arr_board = [[input() for _ in range(4)]]
for _ in range(B-1):
    input()
    arr_board.append([input() for _ in range(4)])
# 입력 끝

di = [0, 1, 0, -1, 1, 1, -1, -1]
dj = [1, 0, -1, 0, 1, -1, 1, -1]
Trie = dict()
score_dict = {
    1: 0,
    2: 0,
    3: 1,
    4: 1,
    5: 2,
    6: 3,
    7: 5,
    8: 11,
}
# 전역 변수 선언 끝

# 트라이 생성
for word in arr_word:
    enTrie(word)
tempTrie = deepcopy(Trie)

# 보글 게임 시작
for board in arr_board:
    ans_list = []
    visited = [[0]*4 for _ in range(4)]
    Trie = deepcopy(tempTrie)

    for i in range(4):
        for j in range(4):
            visited[i][j] = 1
            if board[i][j] in Trie:
                dfs(i, j, board[i][j], Trie[board[i][j]])
            visited[i][j] = 0

    # 정답 구하기
    ans_list.sort()
    max_score = 0
    long_word = ''
    len_long_word = 0
    num_words = len(ans_list)
    for word in ans_list:
        max_score += score_dict[len(word)]
        if len_long_word < len(word):
            len_long_word = len(word)
            long_word = word
    print(max_score, long_word, num_words)