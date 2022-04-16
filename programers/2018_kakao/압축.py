import string
alpha_list = list(string.ascii_uppercase)       # ['A', 'B', ... , 'Z']
num_list = list(range(1, 27))
lzw_dict = dict(zip(alpha_list, num_list))


def lzw(mag):
    last_value = 27
    i = 0
    rlt = []
    while i < len(mag):
        j = 2           # j는 단어 길이. 길이가 1인 단어는 사전에 항상 포함되어 있으므로 2부터 시작
        while mag[i:i+j] in lzw_dict and i+j <= len(mag):
            j += 1

        # 사전에 없다면 등록
        if not mag[i:i+j] in lzw_dict:
            lzw_dict[mag[i:i+j]] = last_value
            last_value += 1

        # 입력을 처리
        rlt.append(lzw_dict[mag[i:i+j-1]])
        i += j - 1
    return rlt


def solution(msg):
    answer = lzw(msg)
    return answer