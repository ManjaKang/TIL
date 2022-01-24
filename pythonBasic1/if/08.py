li = list(range(100,301))
fil = list(filter(lambda a: a%2==0 and int(a/10)%2==0 and int(a/100)%2==0,li))
str_fil = ""
for a in fil:
    str_fil += "%d,"%a
print(str_fil[0:len(str_fil)-1])