arr = list(map(int, input().split()))
ac = list(range(1, 9))
de = list(range(8, 0, -1))
if arr == ac:
    print('ascending')
elif arr == de:
    print('descending')
else:
    print('mixed')