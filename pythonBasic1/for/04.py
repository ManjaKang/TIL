str_i = ""
for i in range(1,101):
    if i%2==1:
        str_i += "%d, "%i
print(str_i[0:len(str_i)-2])
    