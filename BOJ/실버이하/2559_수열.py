N, K = map(int, input().split())
temp_list = list(map(int, input().split()))
sum_list = [0]
temp_sum = 0
for a in temp_list:
    temp_sum += a
    sum_list.append(temp_s)

max_sum = sum_list[K] = sum_list[0]
for i in range(N-K+1):
    temp = sum_list[i+K] - sum_list[i]
    if max_sum < temp:
        max_sum = temp
print(max_sum)