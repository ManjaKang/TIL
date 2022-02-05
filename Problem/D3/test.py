def cal_interval(li):
    result_list = []
    for i in range(1, len(li)):
        interval = li[i]-li[i-1]
        result_list.append(interval)
    return result_list

def cal_interval2(li, k):
    i = 0
    while i < len(li)-1:
        if (li[i]+li[i+1]) <= k:
            li[i] = li[i] + li[i+1]
            li.pop(i+1)
        else:
            i += 1
    return li

a = [0, 1, 3, 7, 8, 9, 10]
b = cal_interval(a)
print(cal_interval(a))
print(cal_interval2(b, 3))