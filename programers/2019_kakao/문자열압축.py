# 문자열 s를 n개 단위로 압축한 길이를 반환하는 함수
def comp(s, n):
    rlt = ''
    prev = ''
    cnt = 1
    for i in range(len(s)//n):
        now = s[i*n:i*n+n]
        if now == prev:
           cnt += 1
        else:
            if cnt != 1:
                rlt += f'{cnt}{prev}'
            else:
                rlt += f'{prev}'        # cnt 가 1일때는 앞에 1을 붙이지 않음
            cnt = 1
        prev = now

    # 문자열의 마지막에 압축이 되었을 때에 rlt에 추가하기 위한 부분
    if now == prev:
        if cnt != 1:
            rlt += f'{cnt}{prev}'
        else:
            rlt += f'{prev}'
    # 문자열 s를 n개 단위로 자르고 남은 부분을 결과에 추가
    rlt += s[(len(s)//n)*n:]
    return len(rlt)


def solution(s):
    answer = 10000
    for i in range(1, len(s)//2+2):
        answer = min(answer, comp(s, i))
    return answer

'''
Test 1 〉	통과 (0.03ms, 10.2MB)
Test 2 〉	통과 (0.31ms, 10.4MB)
Test 3 〉	통과 (0.19ms, 10.3MB)
Test 4 〉	통과 (0.03ms, 10.2MB)
Test 5 〉	통과 (0.01ms, 10.2MB)
Test 6 〉	통과 (0.04ms, 10.2MB)
Test 7 〉	통과 (0.65ms, 10.2MB)
Test 8 〉	통과 (0.58ms, 10.3MB)
Test 9 〉	통과 (0.53ms, 10.4MB)
Test 10 〉	통과 (3.19ms, 10.4MB)
Test 11 〉	통과 (0.07ms, 10.4MB)
Test 12 〉	통과 (0.08ms, 10.2MB)
Test 13 〉	통과 (0.09ms, 10.2MB)
Test 14 〉	통과 (0.90ms, 10.2MB)
Test 15 〉	통과 (0.09ms, 10.2MB)
Test 16 〉	통과 (0.01ms, 10.2MB)
Test 17 〉	통과 (0.87ms, 10.4MB)
Test 18 〉	통과 (0.89ms, 10.4MB)
Test 19 〉	통과 (0.90ms, 10.4MB)
Test 20 〉	통과 (2.08ms, 10.3MB)
Test 21 〉	통과 (2.11ms, 10.2MB)
Test 22 〉	통과 (1.99ms, 10.2MB)
Test 23 〉	통과 (2.14ms, 10.2MB)
Test 24 〉	통과 (2.12ms, 10.2MB)
Test 25 〉	통과 (2.14ms, 10.4MB)
Test 26 〉	통과 (2.04ms, 10.2MB)
Test 27 〉	통과 (1.97ms, 10.2MB)
Test 28 〉	통과 (0.02ms, 10.2MB)
'''