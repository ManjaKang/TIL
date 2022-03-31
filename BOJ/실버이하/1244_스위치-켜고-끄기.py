N = int(input())
sw_list = list(map(int, input().split()))
sw_list.insert(0, 2)
num_students = int(input())
len_sw = len(sw_list)
for _ in range(num_students):
    gender, num = map(int, input().split())
    if gender == 1:
        for i in range(num, len_sw, num):
            sw_list[i] = (sw_list[i] + 1) % 2
    if gender == 2:
        sw_list[num] = (sw_list[num] + 1) % 2
        for i in range(1, len_sw):
            if 1 <= num+i < len_sw and 1 <= num-i < len_sw and sw_list[num+i] == sw_list[num-i]:
                sw_list[num+i] = (sw_list[num+i] + 1) % 2
                sw_list[num-i] = (sw_list[num-i] + 1) % 2
            else:
                break
sw_list.pop(0)
a = len_sw // 20
for i in range(a):
    print(*sw_list[i*20:i*20+20])
print(*sw_list[a*20:a*20+20])