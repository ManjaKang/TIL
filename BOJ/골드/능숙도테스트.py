def go(x):
    if x > 15:
        return
    print(x)
    go(x+2)
    print(x)

go(3)

