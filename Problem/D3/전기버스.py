def cal_interval(li):
    result_list = []
    for i in range(1, len(li)):
        interval = li[i]-li[i-1]
        result_list.append(interval)
    return result_list

def cal_interval2(li, k):
    i = 0
    while i < len(li)-1:
        if (li[i]+li[i+1]) <= k:
            li[i] = li[i] + li[i+1]
            li.pop(i+1)
        else:
            i += 1
    return li

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for t_c in range(1, T + 1):
    K, N, M = map(int, input().split())
    m_list = list(map(int, input().split()))
    # 입력 끝
    m_list.insert(0, 0)
    m_list.append(N)
    ans = 0
    interval_list = cal_interval(m_list)

    if max(interval_list) <= K:
        ans = len(cal_interval2(interval_list, K)) - 1
    print('#{} {}'.format(t_c, ans))
