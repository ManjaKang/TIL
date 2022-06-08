from collections import defaultdict


# 투표인터
def solution(gems):
    num_gems = len(set(gems))
    idx_start, idx_end = 0, 0
    gem_dict = defaultdict(int)
    len_section = float('inf')
    while idx_end < len(gems):
        gem_dict[gems[idx_end]] += 1
        idx_end += 1

        if len(gem_dict) == num_gems:
            while idx_start < idx_end:
                if gem_dict[gems[idx_start]] > 1:
                    gem_dict[gems[idx_start]] -= 1
                    idx_start += 1
                elif len_section > idx_end - idx_start:
                    len_section = idx_end - idx_start
                    answer = [idx_start+1, idx_end]
                    break
                else:
                    break
    return answer


'''
정확성  테스트
Test 1 〉	통과 (0.02ms, 10.1MB)
Test 2 〉	통과 (0.06ms, 10.1MB)
Test 3 〉	통과 (0.16ms, 10.3MB)
Test 4 〉	통과 (0.21ms, 10.2MB)
Test 5 〉	통과 (0.26ms, 10.3MB)
Test 6 〉	통과 (0.01ms, 10.2MB)
Test 7 〉	통과 (0.01ms, 10MB)
Test 8 〉	통과 (0.48ms, 10.3MB)
Test 9 〉	통과 (0.46ms, 10MB)
Test 10 〉	통과 (0.38ms, 10.2MB)
Test 11 〉	통과 (0.49ms, 10.2MB)
Test 12 〉	통과 (0.75ms, 10.2MB)
Test 13 〉	통과 (1.03ms, 10MB)
Test 14 〉	통과 (0.97ms, 10.4MB)
Test 15 〉	통과 (2.12ms, 10.5MB)
효율성  테스트
Test 1 〉	통과 (2.86ms, 10.5MB)
Test 2 〉	통과 (3.92ms, 10.6MB)
Test 3 〉	통과 (8.69ms, 11.1MB)
Test 4 〉	통과 (7.60ms, 11.8MB)
Test 5 〉	통과 (14.03ms, 11.8MB)
Test 6 〉	통과 (15.78ms, 12.1MB)
Test 7 〉	통과 (20.53ms, 12.6MB)
Test 8 〉	통과 (21.23ms, 13.1MB)
Test 9 〉	통과 (27.92ms, 13.5MB)
Test 10 〉	통과 (31.22ms, 13.9MB)
Test 11 〉	통과 (34.69ms, 14.7MB)
Test 12 〉	통과 (26.85ms, 15.5MB)
Test 13 〉	통과 (33.12ms, 16.2MB)
Test 14 〉	통과 (47.67ms, 17MB)
Test 15 〉	통과 (51.52ms, 17.8MB)
'''