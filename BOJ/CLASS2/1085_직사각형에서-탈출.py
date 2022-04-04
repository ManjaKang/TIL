x, y, w, h = map(int, input().split())
a = abs(x-w)
b = abs(y-h)
print(min(a, b, x, y))