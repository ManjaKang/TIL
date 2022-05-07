x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

if (y2 - y1) * (x1 - x3) < (y1 - y3) * (x2 - x1):
    print(-1)
elif (y2 - y1) * (x1 - x3) > (y1 - y3) * (x2 - x1):
    print(1)
else:
    print(0)
