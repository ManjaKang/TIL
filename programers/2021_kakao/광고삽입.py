def solution(play_time: str, adv_time, logs):
    play_hour, play_minute, play_sec = map(int, play_time.split(':'))
    adv_hour, adv_minute, adv_sec = map(int, adv_time.split(':'))
    play_sec += play_hour * 3600 + play_minute * 60
    adv_sec += adv_hour * 3600 + adv_minute * 60
    arr = [0] * (play_sec + 1)
    for log in logs:
        start, end = log.split('-')
        start_hour, start_minute, start_sec = map(int, start.split(':'))
        end_hour, end_minute, end_sec = map(int, end.split(':'))
        start_sec += start_hour * 3600 + start_minute * 60
        end_sec += end_hour * 3600 + end_minute * 60
        arr[start_sec] += 1
        arr[end_sec] -= 1
    # 구간에 시청하고 있는 시청자 수 표시
    for i in range(1, play_sec):
        arr[i] += arr[i-1]
    # 구간합으로 변경
    for i in range(1, play_sec):
        arr[i] += arr[i-1]
    max_viewer = 0
    ans = 0
    for i in range(adv_sec-1, play_sec):
        if arr[i] - arr[i-adv_sec] > max_viewer:
            max_viewer = arr[i] - arr[i-adv_sec]
            ans = i - adv_sec + 1
    ans_hour = str(ans//3600).zfill(2)
    ans_minute = str(ans%3600//60).zfill(2)
    ans_sec = str(ans%60).zfill(2)
    answer = f'{ans_hour}:{ans_minute}:{ans_sec}'
    return answer

'''
Test 1 〉	통과 (1.86ms, 10.5MB)
Test 2 〉	통과 (8.32ms, 10.4MB)
Test 3 〉	통과 (32.18ms, 11.2MB)
Test 4 〉	통과 (259.87ms, 27MB)
Test 5 〉	통과 (351.67ms, 32.5MB)
Test 6 〉	통과 (168.18ms, 21.5MB)
Test 7 〉	통과 (576.15ms, 40.8MB)
Test 8 〉	통과 (630.98ms, 45.7MB)
Test 9 〉	통과 (651.25ms, 54.3MB)
Test 10 〉	통과 (687.65ms, 54.7MB)
Test 11 〉	통과 (759.99ms, 52MB)
Test 12 〉	통과 (719.35ms, 49.7MB)
Test 13 〉	통과 (753.70ms, 54.4MB)
Test 14 〉	통과 (761.22ms, 40.9MB)
Test 15 〉	통과 (69.11ms, 15.1MB)
Test 16 〉	통과 (512.84ms, 40.8MB)
Test 17 〉	통과 (794.90ms, 54.8MB)
Test 18 〉	통과 (753.13ms, 42.1MB)
Test 19 〉	통과 (1.46ms, 10.4MB)
Test 20 〉	통과 (1.58ms, 10.6MB)
Test 21 〉	통과 (150.78ms, 20.2MB)
Test 22 〉	통과 (205.72ms, 20.1MB)
Test 23 〉	통과 (932.32ms, 47.1MB)
Test 24 〉	통과 (702.19ms, 40.9MB)
Test 25 〉	통과 (98.09ms, 19.7MB)
Test 26 〉	통과 (123.81ms, 14.8MB)
Test 27 〉	통과 (102.98ms, 17.3MB)
Test 28 〉	통과 (69.84ms, 16.7MB)
Test 29 〉	통과 (76.36ms, 16.7MB)
Test 30 〉	통과 (46.63ms, 14.1MB)
Test 31 〉	통과 (60.81ms, 14.7MB)
'''