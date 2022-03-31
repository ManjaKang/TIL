input_str = input()
ascii_list = list(map(ord, input_str.upper()))
cnt_list = [0] * 91
for ascii in ascii_list:
    cnt_list[ascii] += 1
if cnt_list.count(max(cnt_list)) >= 2:
    ans = '?'
else:
    ans = chr(cnt_list.index(max(cnt_list)))
print(ans)