# 셔틀버스 문제풀이
# 2022-04-02

# n : 운행 횟수
# t : 배차 간격
# m : 최대 탑승 인원
# timetable : 승객 도착 시간
def solution(n, t, m, timetable):

    times = []
    # 분단위로 받아오기
    for time in timetable:
        hour, minute = map(int, time.split(':'))
        times.append(hour*60 + minute)
    times.sort()
    # 9시 부터 시작
    arrival_time = 540
    front = 0
    while n > 1:
        # 한번에 최대탑승인원만큼 반복
        for _ in range(m):
            if front < len(times) and times[front] <= arrival_time:
                front += 1
            else:
                break
        n -= 1
        arrival_time += t
    temp = times[front:]
    if not temp or len(temp) < m:
        pass
    elif temp[m-1] <= arrival_time:
        arrival_time = temp[m-1] - 1
    h = arrival_time // 60
    min = arrival_time % 60
    answer = str(h).zfill(2) + ':' + str(min).zfill(2)
    return answer