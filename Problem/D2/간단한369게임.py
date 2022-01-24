num = int(input())
for n in range(1, num+1):
    str_n = str(n)
    cnt = 0
    for ch in str_n:
        if (ch == '3') or (ch == '6') or (ch == '9'):
            cnt += 1
    if cnt > 0:
        print('-'*cnt, end = ' ')
    else:
        print(str_n, end = ' ')