# 숫자를 찾아서 체크하는 함수
def check(num):
    for i in range(5):
        for j in range(5):
            if nums_list[i][j] == num:
                check_list[i][j] = 1
                return


# 빙고를 찾을 때 마다 cnt를 1씩 증가
# cnt == 3 이면 True 반환
# for else 문을 사용 for 문이 동작하는 동안 break가 동작하지 않으면 빙고
def check_bingo():
    cnt = 0
    for i in range(5):
        for j in range(5):
            if check_list[i][j] == 0:
                break
        else:
            cnt += 1
            if cnt >= 3:
                return True
    for i in range(5):
        for j in range(5):
            if check_list[j][i] == 0:
                break
        else:
            cnt += 1
            if cnt >= 3:
                return True
    for i in range(5):
        if check_list[i][i] == 0:
            break
    else:
        cnt += 1
        if cnt >= 3:
            return True
    for i in range(5):
        if check_list[i][4-i] == 0:
            break
    else:
        cnt += 1
        if cnt >= 3:
            return True
    return False


nums_list = [list(map(int, input().split())) for _ in range(5)]
moderator_list = [list(map(int, input().split())) for _ in range(5)]
check_list = [[0] * 5 for _ in range(5)]
bingo_list = []
for i in range(5):
    for j in range(5):
        bingo_list.append(moderator_list[i][j])
for i in range(len(bingo_list)):
    check(bingo_list[i])
    if check_bingo():
        ans = i + 1
        break
print(ans)

