# 데이터에서 시 분 초를 초로 변환하고
# 처리시간과 이 값에 1000을 곱해 반환하는 함수
def data_to_sec(line):
    day, time, duration = line.split()
    hour, minute, second = map(float, time.split(':'))
    second += minute * 60 + hour * 3600
    second = int(second * 1000)
    duration = float(duration[:-1])
    duration = int(duration * 1000)
    return second, duration


# 끝 시간과, 처리시간을 받아
# 시작시간과 끝시간을 반환하는 함수
def start_end(second, duration):
    return second - duration + 1, second


def solution(lines):
    start_list = []
    end_list = []
    max_cnt = 0
    # start_list에 시작시간을 저장
    # end_list에 끝시간들을 저장
    for line in lines:
        sec, du = data_to_sec(line)
        start, end = start_end(sec, du)
        start_list.append(start)
        end_list.append(end)

    # 데이터가 정렬되어 있으므로 이전
    # 데이터들은 검사할 필요가 없다.
    for i in range(len(lines)):
        cnt = 1
        now = end_list[i] + 1000
        for j in range(i + 1, len(lines)):
            # 시작시간과 비교하고 있으므로 >=가 아님
            if now > start_list[j]:
                cnt += 1
        max_cnt = max(max_cnt, cnt)
    answer = max_cnt
    return answer