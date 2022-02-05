def verification(sudocu):
    rows = sudocu
    cols = list(map(list, zip(*sudocu)))
    small_row1 = list(map(list, zip(*sudocu[0:3])))
    small_row2 = list(map(list, zip(*sudocu[3:6])))
    small_row3 = list(map(list, zip(*sudocu[6:9])))

    sq1 = [*small_row1[0], *small_row1[1], *small_row1[2]]
    sq2 = [*small_row1[3], *small_row1[4], *small_row1[5]]
    sq3 = [*small_row1[6], *small_row1[7], *small_row1[8]]
    sq4 = [*small_row2[0], *small_row2[1], *small_row2[2]]
    sq5 = [*small_row2[3], *small_row2[4], *small_row2[5]]
    sq6 = [*small_row2[6], *small_row2[7], *small_row2[8]]
    sq7 = [*small_row3[0], *small_row3[1], *small_row3[2]]
    sq8 = [*small_row3[3], *small_row3[4], *small_row3[5]]
    sq9 = [*small_row3[6], *small_row3[7], *small_row3[8]]
    sqs = [sq1, sq2, sq3, sq4, sq5, sq6, sq7, sq8, sq9]

    for row in rows:
        if len(set(row)) < 9:
            return 0
    for col in cols:
        if len(set(col)) < 9:
            return 0
    for sq in sqs:
        if len(set(sq)) < 9:
            return 0
    return 1

T = int(input())

for i in range(1, T+1):
    sudocu = []
    for j in range(9):
        sudocu.append(list(map(int, input().split())))
    verification(sudocu)
    print('#{} {}'.format(i, verification(sudocu)))