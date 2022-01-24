li = list(range(1,201))
fil = list(filter(lambda a: a%7==0 and a%5!=0,li))
str_fil = ""
for a in fil:
    str_fil += "%d,"%a
print(str_fil[0:len(str_fil)-1])