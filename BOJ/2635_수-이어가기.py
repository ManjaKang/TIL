N = int(input())
max_idx = 0
for i in range(1, N+1):
    arr = [N]
    arr.append(i)
    idx = 1
    while arr[idx-1] - arr[idx] >= 0:
        arr.append(arr[idx-1] - arr[idx])
        idx += 1
    if max_idx < idx:
        max_idx = idx
        temp = arr
print('{}'.format(len(temp)))
for a in temp:
    print(a, end=' ')
