from itertools import combinations

T = int(input())
for tc in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    case_list = list(combinations(list(range(N)), N//2))
    x_sum = 0
    y_sum = 0
    vector_min = float('inf')
    for x, y in arr:
        x_sum += x
        y_sum += y
    for case in case_list:
        temp_x = 0
        temp_y = 0
        for now in case:
            temp_x += arr[now][0]
            temp_y += arr[now][1]
        temp_x = x_sum - temp_x*2
        temp_y = y_sum - temp_y*2
        temp_vector = temp_x**2 + temp_y**2
        if temp_vector < vector_min:
            vector_min = temp_vector
    print(vector_min**0.5)