# HH:MM 형태의 시간 문자열을 int 형의 분으로 변환
def time_to_minute(time: str):
    hour, minute = map(int, time.split(':'))
    minute += hour * 60
    return minute


# 올림표가 붙은 음은 소문자로 변환
def sharp(score: str):
    i = 0
    score = list(score)
    while i < len(score):
        if score[i] == '#':
            score[i-1] = score[i-1].lower()
            score.pop(i)
        i += 1
    return ''.join(score)


def solution(m, musicinfos):
    ans = '(None)'
    max_score = 0
    m = sharp(m)
    for music in musicinfos:
        start, end, title, score = music.split(',')
        start = time_to_minute(start)
        end = time_to_minute(end)
        len_radio = end - start
        score = sharp(score)

        # 방송에서 재생한 음표 문자열
        radio = score * (len_radio // len(score)) + score[:len_radio % len(score)]
        if m in radio:
            # 정답이 여러개일 땐 재생 시간이 긴 곡 선택
            if max_score < len_radio:
                max_score = len_radio
                ans = title
    return ans