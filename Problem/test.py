arr = [3, 6, 7, 1, 5, 4]
n = len(arr)

for i in range(1<<n):
    cnt = 0
    part = list()
    for j in range(n):
        # print(bin(i), bin(1<<j),j)
        if i&(1<<j):
            part.append(arr[j])
            cnt += 1

    if cnt == 3:
        print(part)

    part = []