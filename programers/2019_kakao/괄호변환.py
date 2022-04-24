# 올바른 괄호 문자열인지 검사
def is_correct(p):
    temp = 0
    for i in range(len(p)):
        if p[i] == '(':
            temp += 1
        else:
            temp -= 1
        if temp < 0:
            break
    else:
        return True
    return False


def solution(p):
    # 1
    if len(p) == 0:
        return ''
    temp = 0
    u_idx = 0

    # 2
    for i in range(len(p)):
        if p[i] == '(':
            temp += 1
        else:
            temp -= 1
        if temp == 0:
            u_idx = i+1
            break
    u = p[:u_idx]
    v = p[u_idx:]
    # 3
    if is_correct(u):
        # 3-1
        return u + solution(v)
    else:
        # 4
        temp_v = '(' + solution(v) + ')'
        temp_u = ''
        for i in range(1, len(u)-1):
            if u[i] == '(':
                temp_u += ')'
            else:
                temp_u += '('
        return temp_v + temp_u

