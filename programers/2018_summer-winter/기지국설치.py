from math import ceil


def solution(n, stations, w):
    answer = 0
    prev_right = 0
    coverage = 2 * w + 1
    for station in stations:
        left = station - w - 1
        if left - prev_right > 0:
            answer += ceil((left - prev_right) / coverage)
        prev_right = station + w
    if n - prev_right > 0:
        answer += ceil((n - prev_right) / coverage)
    return answer


'''
테스트 1 〉	통과 (1.53ms, 10.4MB)
테스트 2 〉	통과 (1.86ms, 10.4MB)
테스트 3 〉	통과 (1.82ms, 10.4MB)
테스트 4 〉	통과 (1.76ms, 10.4MB)
'''