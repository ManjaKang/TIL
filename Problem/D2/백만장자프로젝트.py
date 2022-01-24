T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    list_price = list(map(int, input().split()))
    selling_price = list_price[-1]
    profit = 0
    for i in range(n-2, -1, -1):
        if list_price[i] < selling_price:
            profit += (selling_price - list_price[i])
        elif list_price[i] > selling_price:
            selling_price = list_price[i]
    print(f'#{test_case} {profit}')
