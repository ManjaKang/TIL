def solution(sticker):
    # 인덱스 에러 방지를 위해 뒤에 리스트 4개를 붙임
    dp1 = sticker[:] + [0] * 4
    dp2 = sticker[:] + [0] * 4
    dp1[2] = dp1[2] + dp1[0]
    dp2[3] = dp2[3] + dp2[1]
    for i in range(3, len(sticker)-1):
        dp1[i] = max(dp1[i-2]+dp1[i], dp1[i-3]+dp1[i])

    for i in range(4, len(sticker)):
        dp2[i] = max(dp2[i-2]+dp2[i], dp2[i-3]+dp2[i])
    answer = max(max(dp2), max(dp1))
    return answer


'''
테스트 1 〉	통과 (70.01ms, 19.1MB)
테스트 2 〉	통과 (73.55ms, 19.1MB)
테스트 3 〉	통과 (74.99ms, 19.1MB)
테스트 4 〉	통과 (74.49ms, 18.9MB)
'''