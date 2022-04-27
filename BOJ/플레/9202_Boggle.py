from copy import deepcopy


def enTrie(word):
    now = Trie
    for ch in word:
        if ch not in now:
            now[ch] = dict()
        now = now[ch]
    now['end'] = word


def dfs(i, j, now, word, board):
    if 'end' in now:
        now.pop('end')
        ans_list.append(word)
        return

    for idx in range(8):
        ni = i + di[idx]
        nj = j + dj[idx]
        if 0 <= ni < 4 and 0 <= nj < 4:
            if visited[ni][nj] == 0 and board[ni][nj] in now:
                visited[ni][nj] = 1
                dfs(ni, nj, now[board[ni][nj]], word + board[ni][nj], board)
                visited[ni][nj] = 0


W = int(input())
arr_word = [input() for _ in range(W)]
input()
B = int(input())
arr_board = []
for _ in range(B-1):
    arr_board.append([input() for _ in range(4)])
    input()
arr_board.append([input() for _ in range(4)])
# 입력 끝

di = [0, 1, 0, -1, 1, 1, -1, -1]
dj = [1, 0, -1, 0, 1, -1, 1, -1]
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
visited = [[0] * 4 for _ in range(4)]
Trie = dict()
for word in arr_word:
    enTrie(word)
temp_Trie = deepcopy(Trie)

for board in arr_board:
    Trie = deepcopy(temp_Trie)
    ans_list = []
    for i in range(4):
        for j in range(4):
            visited[i][j] = 1
            dfs(i, j, Trie, '', board)
            visited[i][j] = 0
    max_score = 0
    longest_word = ''
    longest_Length = 0
    num_word = len(ans_list)
    for ans_word in ans_list:
        max_score += score_dict[len(ans_word)]
        if longest_Length < len(ans_word):
            longest_Length = len(ans_word)
            longest_word = ans_word
    print(max_score, longest_word, num_word)
