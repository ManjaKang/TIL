a = list(range(1,101))
b = list(filter(lambda i : i%2==0, a))
for i in b:
    print(b,a)