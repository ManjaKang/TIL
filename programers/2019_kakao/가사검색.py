# 첫 번째 시도
import re


def questionToDot(s):

    def change(ch):
        if ch == '?':
            return '.'
        else:
            return ch

    return ''.join(list(map(change, s)))


def solution(words, queries):
    comp_list = []
    answer = []
    for query in queries:
        temp = re.compile(questionToDot(query))
        comp_list.append(temp)

    for i, comp in enumerate(comp_list):
        cnt = 0
        for word in words:
            if len(word) == len(queries[i]) and comp.match(word):
                cnt += 1
        answer.append(cnt)
    return answer


'''
Test 1 〉	실패 (시간 초과)
Test 2 〉	실패 (시간 초과)
Test 3 〉	실패 (시간 초과)
Test 4 〉	통과 (576.83ms, 15.4MB)
Test 5 〉	통과 (1395.29ms, 21.8MB)
'''
