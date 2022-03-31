def interval(arr):
    max_interval = 0
    for i in range(len(arr)-1):
        temp = arr[i+1]-arr[i]
        if max_interval < temp:
            max_interval = temp
    return max_interval


W, L = map(int, input().split())
N = int(input())
width_list = [0]
lengh_list = [0]
for _ in range(N):
    flag, num = map(int, input().split())
    if flag == 0:
        lengh_list.append(num)
    if flag == 1:
        width_list.append(num)
lengh_list.append(L)
width_list.append(W)
lengh_list.sort()
width_list.sort()
w_max = interval(width_list)
l_max = interval(lengh_list)
print(w_max * l_max)
