# 간단한 투포인터

def solution(A: list, B: list):
    A.sort()
    B.sort()
    answer = 0
    i = 0
    for b in B:
        if b > A[i]:
            answer += 1
            i += 1
    return answer


'''
테스트 1 〉	통과 (42.51ms, 18.5MB)
테스트 2 〉	통과 (42.06ms, 18.3MB)
테스트 3 〉	통과 (38.96ms, 18.3MB)
'''