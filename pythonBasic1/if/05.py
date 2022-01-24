ch = input()
ch2 = ''
if ch.isupper():
    ch2 = ch.lower() 
elif ch.islower():
    ch2 = ch.upper()
print("%s(ASCII: %d) => %s(ASCII: %d)"%(ch,ord(ch),ch2,ord(ch2)))