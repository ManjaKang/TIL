def solution(n, t, m, p):
    n_str = n_game(n, t, m)
    answer = ''
    for i in range(t):
        answer += n_str[p+i*m-1] # 전체 n 게임 문자열에서 내 차례 문자열만 선택하는 함수
    return answer


# 전체 n 게임 문자열을 구하는함수
def n_game(n, t, m):
    rlt = ''
    i = 0
    while True:
        for ch in n_notation(i, n):
            rlt += ch
            if len(rlt) == m*t:
                return rlt
        i += 1


# 숫자를 n진법의 문자열로 변환하는 함수
def n_notation(i, n):
    if i == 0:
        return '0'
    rlt = ''
    while i > 0:
        rlt = hex(i % n)[2:].upper() + rlt      # '0xff' >> 'FF' 로 변환
        i //= n
    return rlt


print(solution(16, 16, 2, 2))
