from itertools import permutations
import re


def solution(user_id, banned_id):
    pattern_list = []
    ans_list = []
    for ban in banned_id:
        pattern_list.append(ban.replace('*', '.'))

    for case in permutations(user_id, len(banned_id)):
        for user, pattern in zip(case, pattern_list):
            if len(user) == len(pattern) and re.match(pattern, user):
                continue
            else:
                break
        else:
            temp = sorted(list(case))
            if temp not in ans_list:
                ans_list.append(temp)
    return len(ans_list)


users = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
ban = ["fr*d*", "*rodo", "******", "******"]
print(solution(users, ban))
