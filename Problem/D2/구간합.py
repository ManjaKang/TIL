T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for t_c in range(1, T + 1):
    N, M = map(int, input().split())
    m_list = list(map(int, input().split()))
    su_list = []
    for i in range(0,N-M+1):
        cnt = 0
        su = 0
        while cnt < M:
            su += m_list[i+cnt]
            cnt += 1
        su_list.append(su)
    
    sub = max(su_list) - min(su_list)
    print('#{} {}'.format(t_c, sub))
