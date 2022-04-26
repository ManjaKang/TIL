def is_correct(word, query, direction, point):
    if len(word) != len(query):
        return False

    if direction == 'both':
        return True

    if direction == 'front':
        for i in range(point, len(word)):
            if word[i] != query[i]:
                return False
        return True

    if direction == 'back':
        for i in range(point):
            if word[i] != query[i]:
                return False
        return True


def find_mark(query):
    if query[0] == '?' and query[-1] == '?':
        return 'both', 0

    if query[0] == '?':
        front = 0
        end = len(query) - 1
        while end >= front:
            mid = (end + front) // 2
            if query[mid] == '?':
                front = mid + 1
            else:
                end = mid - 1
        return 'front', front
    else:
        front = 0
        end = len(query) - 1
        while end >= front:
            mid = (end + front) // 2
            if query[mid] != '?':
                front = mid + 1
            else:
                end = mid - 1
        return 'back', front


def solution(words, queries):
    answer = [0] * len(queries)
    for i, query in enumerate(queries):
        direction, point = find_mark(query)
        for word in words:
            if is_correct(word, query, direction, point):
                answer[i] += 1
    return answer